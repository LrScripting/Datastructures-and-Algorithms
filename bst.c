#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left, *right;
};

//func to create new bst 
struct node* newNode(int data)
{
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
};

struct node* insert(struct node* node, int data){
    if (node == NULL)return newNode(data);
    
    if (data < node->data){
        node->left = insert(node->left, data);
    }
    else if (data > node->data){
        node->right = insert(node->right, data);
    }
    return node;
};
// gives nodes in non decreasing order
void inorder(struct node* root)
{
 
    if (root != NULL){
        //calls itself on each of the nodes first to the left, once it reaches the lowest node it prints itself, then calls the function on the right node.
        inorder(root->left);
        printf("%dy ", root->data);
        inorder(root->right);
        
    }
}
// used to copy a tree
void preorder(struct node* root){
   
    if(root != NULL){
        printf("%dx ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}
// prints leaf nodes, leaf nodes are nodes with no child nodes
// this func recursively calls itself on its left and right nodes and return once its passed a null value
// if its passed a value whos left and right nodes contain null then it prints the nodes data
void printLeaves(struct node* node){
    if(!node){
        return;
    }
    else{
        if(!node->left && !node->right){
            printf("%d ", node->data);
        }
        if(node->left){
            printLeaves(node->left);
        }
        if(node->right){
            printLeaves(node->right);
        }
    }
}
void printnonLeaves(struct node* node) {
    if(!node){
        return;
    }
    else{
        if(node->left || node->right){
            printf("%d ", node->data);
        }
        if(node->left){
            printnonLeaves(node->left);
        }
        if(node->right){
            printnonLeaves(node->right);
        }
        }
    }

//similar to a pre order but prints left sub tree, then the right subtree, followed by the root
//useful for deleting bst's

void postOrder(struct node* root){
    if (root != NULL){
        postOrder(root->left);
        postOrder(root->right);
        printf("%dz ", root->data);
    }


}


//calc height for level order function 

int height(struct node* node){
    if (node == NULL){
        return 0;
    }
    else{
        int leftLength = height(node->left);
        int rightLength = height(node->right);
     
       
        if(leftLength > rightLength){
            
            return (leftLength + 1);
        }
        else{
            return (rightLength + 1);
        }
    }
}
void Level(struct node* root, int level){
    if (root == NULL){
        return;
    }
    if(level == 1){
        printf("%d " , root->data);
    }
    else{
        Level(root->left, level-1);
        Level(root->right, level-1);
    }
}


void levelOrder(struct node* root){
    int h = height(root);
    int i;
    for(i = 1; i <= h; i++){
        Level(root, i);
        printf("\n");
    }
};


//right view of the nodes
void rightLeaves(struct node* node, int level, int* maxLevel){
    if(!node){
        return;
    }
    else{

        // if the is final node
        if(*maxLevel < level){
            printf("%d\t", node->data);
            *maxLevel = level;
        }

        //go through right then left subtree
        rightLeaves(node->right, level + 1, maxLevel);
        rightLeaves(node->left, level + 1, maxLevel);

    }
    
}

void printRightLeaves(struct node* node){
    int maxLevel = 0;
    rightLeaves(node, 1, &maxLevel);
}
void myviewright(struct node* node){
    if(!node){
        return;
    }
    else{
        printf("%d ", node->data);
        if(node->right){
            myviewright(node->right);
        }
    }
}

void myleftview(struct node* node){
    if(!node){
        return;
    }
    else{
        printf("%d ", node->data);
        myleftview(node->left);
    }
}
struct node* emptyTree(struct node* root){
    struct node* temp;
    if(!root){
        return NULL;
    }
    else{
        emptyTree(root->left);
        emptyTree(root->right);
        temp = root;
        free(temp);
    }
    return root;
}
void leftLeaves(struct node* node, int level, int* maxLevel){
    if(!node){
        return;
    }
    else{
        if(*maxLevel < level){
            printf("%d\t", node->data);
            *maxLevel = level;
        }

        //go through right then left subtree
        leftLeaves(node->left, level + 1, maxLevel);
        leftLeaves(node->left, level + 1, maxLevel);
    }
}
void printLeftLeaves(struct node* node){
    int maxLevel = 0;
    leftLeaves(node, 1, &maxLevel);
}

// delete node of a specific key

void replaceElement(struct node* root, int data, int replacementData){
    if(!root){
        return;
    }    
    else{
        if(data > root->data){
            replaceElement(root->right, data, replacementData);
        }
        if(data < root->data){
            replaceElement(root->left, data, replacementData);
        }
        if(data == root->data){
            root->data = replacementData;
        }
    }
}
struct node* minvalue(struct node* node){
    if(!node){
        return NULL;
    }
        if(node){
            struct node* current;
            minvalue(node->left);
            current = node;
            if(!node->left){
                return current;
            }   
        
    }
}
int nodeCount(struct node* node)
{
    if (node == NULL)
        return 0;
 
    else
        return nodeCount(node->left)
               + nodeCount(node->right) + 1;
}
struct node* deleteNode(struct node* node, int data){
    
    if(!node){
        return NULL;
    }
    else{
        if(data > node->data){
            deleteNode(node->right, data);
        }
        else if(data < node->data){
            deleteNode(node->right, data);
        }
        else{
            if(node->right == NULL){
                struct node* temp;
                temp = node->left;
                free(node);
                return temp;
            }
            else if(node->left == NULL){
                struct node* temp;
                temp = node->right;
                free(node);
                return temp;
            }

            struct node* temp = minvalue(node->right);
            node->data = temp->data;
            node->right = deleteNode(node->right, temp->data);
        }
        return node;
    }
}
int main(){
    struct node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    insert(root, 10);
    
    //preorder(root);
    //inorder(root);
    //postOrder(root);
    //levelOrder(root);
    //printLeaves(root);
    //printnonLeaves(root);
    //printRightLeaves(root);
    //myviewright(root);
    //printLeftLeaves(root);
   // myleftview(root);
    //replaceElement(root, 70, 22);
   //replaceElement(root, 20, 31);
    levelOrder(root);
    emptyTree(root);
    levelOrder(root);
    //deleteNode(root, 80);
    //levelOrder(root);
    
    //minvalue(root);
    return 0;
}
