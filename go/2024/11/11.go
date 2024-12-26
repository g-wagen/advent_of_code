package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func toIntSlice(file *os.File) []int {
	output := []int{}
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()
		for _, num := range strings.Split(text, " ") {
			number, _ := strconv.Atoi(string(num))
			output = append(output, number)
		}
	}

	return output
}

func sortMapKeys(m map[int]int) []int {
	keys := []int{}
	for item, _ := range m {
		keys = append(keys, item)
	}
	slices.Sort(keys)
	return keys
}

func blink(stones []int, count int) int {
	newStones := make([]int, len(stones))
	copy(newStones, stones)

	for b := 0; b < count; b++ {
		out := []int{}
		for _, stone := range newStones {
			digits := countDigits(stone)
			even := digits%2 == 0
			if stone == 0 {
				out = append(out, 1)
			} else if even {
				temp := fmt.Sprintf("%d", stone)
				left, _ := strconv.Atoi(temp[:digits/2])
				right, _ := strconv.Atoi(temp[digits/2:])
				out = append(out, left, right)
			} else if stone != 0 && even == false {
				out = append(out, stone*2024)
			}
		}
		newStones = out
	}

	return len(newStones)
}

func blinkOpti(stones []int, count int) int {
	cache := make(map[int]int)

	for _, stone := range stones {
		cache[stone]++
	}

	for b := 0; b < count; b++ {
		tempCache := make(map[int]int)

		for stone, quantity := range cache {
			if quantity == 0 {
				continue
			}

			digits := countDigits(stone)
			even := digits%2 == 0

			if stone == 0 {
				tempCache[1] += quantity
			} else if even {
				temp := fmt.Sprintf("%d", stone)
				left, _ := strconv.Atoi(temp[:digits/2])
				right, _ := strconv.Atoi(temp[digits/2:])
				tempCache[left] += quantity
				tempCache[right] += quantity
			} else {
				tempCache[stone*2024] += quantity
			}
		}

		cache = tempCache
	}

	totalStones := 0
	for _, quantity := range cache {
		totalStones += quantity
	}

	return totalStones
}

func countDigits(num int) int {
	if num == 0 {
		return 1
	}
	count := 0
	for num > 0 {
		num /= 10
		count++
	}
	return count
}

func d11p1(file *os.File) int {
	input := toIntSlice(file)
	numStones := blink(input, 25)
	return numStones
}

func d11p2(file *os.File) int {
	input := toIntSlice(file)
	numStones := blinkOpti(input, 75)
	return numStones
}

func main() {
	file, _ := os.Open(os.Args[1])
	defer file.Close()

	fmt.Println("Solution Day 11 Part 1:", d11p1(file))
	file.Seek(0, 0)
	fmt.Println("Solution Day 11 Part 2:", d11p2(file))
}
