#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it.
 * @head: pointer to linked list.
 * Return: 0 if it doesn't have a cycle in it or 1 if it does.
 */

int check_cycle(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	if (head == NULL || head->next == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
