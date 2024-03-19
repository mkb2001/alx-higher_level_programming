#include "lists.h"

listint_t *createNode(int data) {
    listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->n = data;
    newNode->next = NULL;
    return newNode;
}

listint_t *insert_node(listint_t **head, int number) {
    listint_t *newNode = createNode(number);

    listint_t *current = *head;
    listint_t *prev = NULL;


    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }


    if (prev == NULL) {
        newNode->next = *head;
        *head = newNode;
    } else {
        prev->next = newNode;
        newNode->next = current;
    }

    return newNode;
}

