const list1 = [1, 2, 4];
const list2 = [1, 3, 4];

function mergeList() {
    function ListNode(val, next) {
            this.val = (val===undefined ? 0 : val)
            this.next = (next===undefined ? null : next)
        }

    let mergedList = new ListNode();

    for (let i = 0; i < list1.length; i++) {
        mergedList.val = new ListNode(list1[i]);
        mergedList.next = new ListNode(list2[i]);
    }

    console.log(mergedList);
}

mergeList();