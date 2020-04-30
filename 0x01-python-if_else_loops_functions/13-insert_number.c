#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert a new node in ordened way.
 * @head: Linked list's head.
 * @number: Number to add within.
 *
 * Return: It returns the address to the new node, on failure NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	int x = 0;
	listint_t *current = NULL, *next = NULL, *new_node;

	if (!head)
		return (NULL);

	if (*head)
		next = *head, current = next;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if ((next != NULL && (number < next->n)) || !(*head))
		new_node->next = *head, *head = new_node, x = 1;

	for (; next && x == 0; current = next, next = next->next)
	{
		if (number < next->n)
		{
			new_node->next = next, current->next = new_node;
			break;
		}
	}

	if ((!next && x == 0))
		current->next = new_node, new_node->next = NULL;

	return (new_node);
}