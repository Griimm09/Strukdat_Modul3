class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def search(self, item):
        try:
            idx = self.items.index(item)
            return self.size() - idx
        except ValueError:
            return -1
        
st = Stack()

st.push("Aku")
st.push("Anak")
st.push("Indonesia")

print("Next : ", st.peek())
st.push("Raya")
print(st.pop())
st.push("!")

count = st.search("Aku")
while count != -1 and count > 1:
    st.pop()
    count -= 1

print(st.pop())
print(st.is_empty())