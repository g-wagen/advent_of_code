package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	file, error := os.Open(os.Args[1])

	if error != nil {
		fmt.Println(error)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	total := 0

	for scanner.Scan() {
		puzzleInput := scanner.Text() //`xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
		pattern := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)

		found := pattern.FindAllString(puzzleInput, -1)
		for _, v := range found {
			subPattern := regexp.MustCompile(`\d+`)
			multis := subPattern.FindAllString(v, -1)
			mults := []int{}

			for _, m := range multis {
				conv, _ := strconv.Atoi(m)
				mults = append(mults, conv)
			}
			total = total + mults[0]*mults[1]
		}
	}
	fmt.Println(total)
}
