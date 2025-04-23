const list1 = [1, 2, 4];
const list2 = [1, 3, 4];

function ListNode(data) {
    this.data = data;
    this.next = null;
}

function SinglyLinkedList() {
    this.head = null;
    this.size = 0;
}

SinglyLinkedList.prototype.insert = function (data) {
    if (this.head === null) {
        this.head = new ListNode(data);
    } else {
        let head = this.head;
        while (head.next !== null) {
            head = head.next;
        }
        head.next = new ListNode(data);
    }
}

SinglyLinkedList.prototype.print = function () {
    let currentNode = this.head;

    while (currentNode) {
        console.log(currentNode.data);
        currentNode = currentNode.next;
    }

    console.log("Null");
}

let linkedList = new SinglyLinkedList();
linkedList.insert(1);
linkedList.insert(2);
linkedList.insert(3);

linkedList.print();