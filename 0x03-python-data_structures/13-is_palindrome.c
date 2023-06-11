#include "lists.h"

/**
 * reverse_linked_list - reverses single linked list
 * @head: pointer to pointer to the head of the linked list.
 * Return: pointer to head
 */

listint_t *reverse_linked_list(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *prev = NULL;
	listint_t *node;

	while (temp != NULL)
	{
		node = temp->next;
		temp->next = prev;
		prev = temp;
		temp = node;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if the linked list is palindrome or not.
 * @head: pointer to pointer to the head of the linked list.
 * Return: 0 if the linked list is palindrome, or 1 if it'S not.
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t len = 0;
	size_t i = 0;

	temp = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	temp = *head;
	while (i < (len / 2) - 1)
	{
		temp = temp->next;
		i++;
	}
	if (temp->n != temp->next->n && (len % 2) == 0)
		return (0);
	temp = temp->next->next;
	rev = reverse_linked_list(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_linked_list(&mid);
	return (1);
}
