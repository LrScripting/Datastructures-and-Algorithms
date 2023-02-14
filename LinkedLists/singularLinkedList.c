#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node* next;
};

//provided a reference to the head pointer
// add an item to the linked list

void push(struct node** head, int data){
    struct node* node = (struct node*)malloc(sizeof(struct node));

    node->data = data;
    node->next = (*head);
    (*head) = node;
}

void printNodes(struct node* node){
    while(node){
        printf("%d ", node->data);
        node = node->next;

    }
}
int listlen(struct node* head){
    if(!head){
        return 0;
    }
    else{
        return listlen(head->next) + 1;
    }
}
int listSize(struct node* head){
  int c = 0;
  while(head){
    c+=1;
    head = head->next;
  }
  return c;
}

void newHead(struct node** head, int data){
    struct node* new1 = (struct node*)malloc(sizeof(struct node));
    new1->data = data;
    new1->next = *head;
    *head = new1;
}

void newEnd(struct node** head, int data){
    struct node* new1 = (struct node*)malloc(sizeof(struct node));
    new1->data = data;
    new1->next = NULL;
    struct node *temp = *head;
    
    while(temp != NULL){
        temp = temp->next;

    }
    temp->next = new1;
}

void appendAfter(struct node* prev, int data){
    if(!prev){
        return;
    }
    else{
        struct node* new1 = (struct node*)malloc(sizeof(struct node));
        new1->data = data;
        new1->next = prev->next;
        prev->next = new1;

    }
}


int main(){
    struct node* first = NULL;
    push(&first, 10);
    push(&first, 20);
    push(&first, 30);
    push(&first, 40);
    push(&first, 50);
    newEnd(first, 25);
    printNodes(first);
    printf("%d", listlen(first));
    //printf("%d ListLength: ", listSize(first));
}
