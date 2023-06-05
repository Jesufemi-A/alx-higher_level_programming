#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a circle in a linked_list
 * @list: the head node
 * Return: 1 if there is a circle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *bolt;
	listint_t *snail;

	if (list == NULL || list->next == NULL)
		return (0);
	bolt = list;
	snail = list;
	while (bolt != NULL && bolt->next != NULL)
	{
		bolt = bolt->next->next;
		snail = snail->next;
		if (bolt == snail)
			return (1);
	}
	return (0);
}
