#include "lists.h"

/**
* check_cycle - a function in C that checks if a singly linked list has a cycle in it.
* @
*/
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while(slow != NULL && fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
        if (fast == slow)
        {
            return (1);
        }
    }
    return (0);
}
