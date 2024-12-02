package main

import (
    "bufio"
    "fmt"
    "os"
    "slices"
    "strings"
    "sort"
    "strconv"
)

func main() {
    file, error := os.Open("02-input.txt")
    
    if error != nil {
        fmt.Println(error)
        return
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)

    total := 0

    for scanner.Scan() {
        fields := strings.Fields(scanner.Text())
        fieldsi := []int{}

        for _, v := range fields {
            iv, _ := strconv.Atoi(v)
            fieldsi = append(fieldsi, iv)
        }

        fieldsir := []int{}
        
        for _, v := range fieldsi {
            fieldsir = append(fieldsir, v)
        }
        
        slices.Reverse(fieldsir)
        
        if sort.IntsAreSorted(fieldsi) {
            fmt.Println(fieldsi, "ascending")
            
            lastnum := fieldsi[0]
            safe := 0
            optimal := len(fields)-1

            for i, v := range fieldsi {
                if i > 0 && v - fieldsi[i-1] <= 3 && v - fieldsi[i-1] >= 1 {
                    safe++
                }
                lastnum = v
            }
            fmt.Println(optimal, safe, lastnum)

            if optimal == safe {
                total++
            }
        }

        if sort.IntsAreSorted(fieldsir) {
            fmt.Println(fieldsi, "descending")
            
            lastnum := fieldsir[0]
            safe := 0
            optimal := len(fields)-1

            for i, v := range fieldsir {
                if i > 0 && v - fieldsir[i-1] <= 3 && v - fieldsir[i-1] >= 1 {
                    safe++
                }
                lastnum = v
            }
            fmt.Println(optimal, safe, lastnum)

            if optimal == safe {
                total++
            }
        }
    }
    fmt.Println(total)
}
