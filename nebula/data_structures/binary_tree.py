from typing import Generic, Iterable, Any, TypeVar

T = TypeVar("T", bound="Comparable")
S = TypeVar("S", bound="Comparable")


class Comparable:
    def __lt__(self, other):
        return NotImplemented

    def __eq__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other


class TreeNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: T):
        """
        Insert a value into the tree.
        """
        parent = self
        while parent:
            if value < parent.value:
                if parent.left is None:
                    parent.left = TreeNode(value)
                    return
                parent = parent.left
            elif value > parent.value:
                if parent.right is None:
                    parent.right = TreeNode(value)
                    return
                parent = parent.right
            else:
                return

    def inorder(self):
        """
        Inorder traversal of the tree.
        """
        if self.left:
            yield from self.left.inorder()
        yield self.value
        if self.right:
            yield from self.right.inorder()

    def preorder(self):
        """
        Preorder traversal of the tree.
        """
        yield self.value
        if self.left:
            yield from self.left.preorder()
        if self.right:
            yield from self.right.preorder()

    def postorder(self):
        """
        Postorder traversal of the tree.
        """
        if self.left:
            yield from self.left.postorder()
        if self.right:
            yield from self.right.postorder()
        yield self.value

    def __iter__(self):
        yield from self.inorder()

    def __contains__(self, value: T) -> bool:
        if value == self.value:
            return True
        if value < self.value:
            return self.left.__contains__(value) if self.left else False
        else:
            return self.right.__contains__(value) if self.right else False

    def __len__(self):
        return sum(1 for _ in self)

    def __repr__(self):
        return f"TreeNode({self.value})"


class BinaryTree(Generic[T]):
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, value: T):
        """
        Insert a value into the tree.
        """
        if self._root is None:
            self._root = TreeNode(value)
        else:
            self._root.insert(value)

    def inorder(self):
        """
        Inorder traversal of the tree.
        """
        if self._root:
            return self._root.inorder()
        return iter([])

    def preorder(self):
        """
        Preorder traversal of the tree.
        """
        if self._root:
            return self._root.preorder()
        return iter([])

    def postorder(self):
        """
        Postorder traversal of the tree.
        """
        if self._root:
            return self._root.postorder()
        return iter([])

    @staticmethod
    def from_iterable[S](iterable: Iterable[S]) -> "BinaryTree":
        """
        Create a binary tree from an iterable.
        """
        tree = BinaryTree[S]()
        for value in iterable:
            tree.insert(value)
        return tree

    def __iter__(self):
        if self._root:
            yield from self._root
        return iter([])

    def __len__(self):
        return self._root.__len__() if self._root else 0

    def __contains__(self, value: Any):
        return value in self._root if self._root else False

    def __add__(self, other: "BinaryTree"):
        """
        Add two trees together.
        """
        new_tree = BinaryTree()
        for value in self:
            new_tree.insert(value)
        for value in other:
            new_tree.insert(value)
        return new_tree

    def __getitem__(self, key) -> T:
        """
        Get an item from the tree.
        """
        if isinstance(key, int):
            if key < 0:
                raise IndexError("Index must be non-negative.")
            for i, value in enumerate(self):
                if i == key:
                    return value
            raise IndexError("Index out of range.")
        elif isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self[i] for i in range(start, stop, step)]
        else:
            raise TypeError("Invalid key type.")

    def __repr__(self):
        return f"BinaryTree({list(self)})"
