#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * struct Node - linked list node
 * @n: integer
 * @next: points to the next node
 */
typedef struct Node
{
    int n;
    struct Node *next;
} Node;

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the linked list
 * @number: number to insert
 *
 * Return: pointer to the new node or NULL on failure
 */
Node *insert_node(Node **head, int number)
{
    Node *new_node, *current;

    if (!head)
        return (NULL);

    new_node = malloc(sizeof(Node));
    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (!*head || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;
    while (current->next && number > current->next->n)
        current = current->next;

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}

