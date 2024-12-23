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

	appendage := 0
	for i, number := range diskMap {
		if i%2 == 0 {
			appendage = i / 2
		} else {
			appendage = -1
		}
		for j := 0; j != number; j++ {
			unpacked = append(unpacked, appendage)
		}
	}

	return unpacked
}

func moveBlocks(unpacked []int) []int {
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
		if num >= 0 {
			sum += i * num
		}
	}

	return sum
}

func count(s []int, n int) int {
	out := 0
	for _, item := range s {
		if item == n {
			out++
		}
	}
	return out
}

func makeSlice(l int, d int) []int {
	sl := make([]int, l)
	for i := 0; i < l; i++ {
		sl[i] = d
	}
	return sl
}

func moveFiles(data []int) []int {
	countdown := slices.Max(data)

	for countdown > 0 {
		need := count(data, countdown)

		space := makeSlice(need, -1)
		numbers := makeSlice(need, countdown)

		index := slices.Index(data, countdown)

		for i := 0; i < len(data); i++ {
			have := data[i : need+i]
			if slices.Equal(have, space) && index > i {
				for slices.Index(data, countdown) > -1 {
					data[slices.Index(data, countdown)] = -1
				}
				data = slices.Replace(data, i, i+need, numbers...)
				break
			}
		}
		countdown--
	}
	return data
}

func d9p1(file *os.File) int {
	input := readInput(file)
	unpacked := unpack(input)
	moved := moveBlocks(unpacked)

	return checksum(moved)
}

func d9p2(file *os.File) int {
	input := readInput(file)
	unpacked := unpack(input)
	moved := moveFiles(unpacked)

	return checksum(moved)
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
