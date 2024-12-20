package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
)

func readInput(file *os.File) []int {
	output := []int{}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		text := scanner.Text()
		for _, char := range text {
			number, _ := strconv.Atoi(string(char))
			output = append(output, number)
		}
	}
	return output
}

func unpack(diskMap []int) []int {
	unpacked := []int{}

	fileId := 0

	for i, number := range diskMap {
		if i%2 == 0 {
			for j := 0; j != number; j++ {
				unpacked = append(unpacked, fileId)
			}
			fileId++
		} else {
			for j := 0; j != number; j++ {
				unpacked = append(unpacked, -1)
			}
		}
	}

	return unpacked
}

func pack(unpacked []int) []int {
	for slices.Index(unpacked, -1) > -1 {
		s := slices.Index(unpacked, -1)
		unpacked[s] = unpacked[len(unpacked)-1]
		unpacked = unpacked[:len(unpacked)-1]
	}

	return unpacked
}

func checksum(packed []int) int {
	sum := 0

	for i, num := range packed {
		sum += i * num
	}

	return sum
}

func d9p1(file *os.File) int {
	input := readInput(file)

	unpacked := unpack(input)
	packed := pack(unpacked)

	return checksum(packed)
}

func d9p2(file *os.File) int {
	checksum := 0

	//input := readInput(file)
	//fmt.Println(input)

	return checksum
}

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}

	defer file.Close()

	fmt.Println("Solution Day 9 Part 1:", d9p1(file))

	file.Seek(0, 0)

	fmt.Println("Solution Day 9 Part 2:", d9p2(file))
}
