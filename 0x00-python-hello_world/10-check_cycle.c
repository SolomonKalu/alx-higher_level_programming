#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle.
 *
 * @list: The pointer to the linked list
 *
 * Return: 0 if no, 1 if a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *new1 = list;
	listint_t *new2 = list;

	while(new1 && new2 && new2->next)
	{
		new1 = new1->next;
		new2 = new2->next->next;
		if (new2 == new1)
			return (1);
	}

	return (0);
}
