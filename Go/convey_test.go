package main

import (
	"testing"
	. "github.com/smartystreets/goconvey/convey"
)

//leetcode submit region end(Prohibit modification and deletion)
//go mod init main <packagename>下才可以
//go get github.com/smartystreets/goconvey
//更换国内源
//$ export GO111MODULE=on
//$ export GOPROXY=https://goproxy.cn,direct

//go run 191_number-of-1-bits.go

//go test -v 191_number-of-1-bits.go convey_test.go
//go test -v *.go

func TestFib(t *testing.T) {
	var fibTests = []struct {
		in       int // input
		expected int // expected result
	}{
		{1, 1},
		{2, 1},
		{3, 2},
		{4, 3},
		{5, 5},
		{6, 8},
		{7, 13},
	}

	for _, tt := range fibTests {
		actual := Fib(tt.in)
		if actual != tt.expected {
			t.Errorf("Fib(%d) = %d; expected %d", tt.in, actual, tt.expected)
		}
	}
}

func Test0191(t *testing.T) {

	// Only pass t into top-level Convey calls
	Convey("Given some integer with a starting value", t, func() {
		var x uint32 = 00000000000000000000000000001011
		So(hammingWeight(x), ShouldEqual, 3)

	})
}

func TestSpec(t *testing.T) {

	// Only pass t into top-level Convey calls
	Convey("Given some integer with a starting value", t, func() {
		x := 1

		Convey("When the integer is incremented", func() {
			x++

			Convey("The value should be greater by one", func() {
				So(x, ShouldEqual, 2)
			})
		})
	})
}

func TestStringSliceEqual0(t *testing.T) {
	Convey("TestStringSliceEqual的描述", t, func() {
		a := []string{"hello", "goconvey"}
		b := []string{"hello", "goconvey"}
		So(StringSliceEqual(a, b), ShouldBeTrue)
	})
}

func TestStringSliceEqual(t *testing.T) {
	Convey("TestStringSliceEqual", t, func() {
		Convey("true when a != nil  && b != nil", func() {
			a := []string{"hello", "goconvey"}
			b := []string{"hello", "goconvey"}
			So(StringSliceEqual(a, b), ShouldBeTrue)
		})

		Convey("true when a ＝= nil  && b ＝= nil", func() {
			So(StringSliceEqual(nil, nil), ShouldBeTrue)
		})
	})
}
