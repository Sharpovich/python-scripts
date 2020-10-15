/*
Даны два числа. Определить цифры, входящие в запись
как первого, так и второго числа.

Выходные данные
Программа должна вывести цифры,
которые имеются в обоих числах, через пробел.
Цифры выводятся в порядке их нахождения в первом числе.*/
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var left, right int = 564, 8954
	left1, right1 := strconv.Itoa(left), strconv.Itoa(right)
	fmt.Println(left1, right1) //debugString
	var numeric []int
	for i := 0; i < len(left1); i++ {
		for k := 0; k < len(right1); k++ {
			if string(left1[i]) == string(right1[k]) {
				i, _ := strconv.Atoi(string(left1[i]))
				numeric = append(numeric, i)
				break
			}

		}
	}
	for _, i := range numeric {
		fmt.Print(strconv.Itoa(i) + " ")
	}
}

