package main

//go get -u gopkg.in/check.v1

import (
	. "gopkg.in/check.v1"
	"io"
	"testing"
)

func TestSim(t *testing.T) { TestingT(t) } //继承testing的方法，可以直接使用go test命令运行

type MySuiteSim struct{} //创建测试套件结构体

var _ = Suite(&MySuiteSim{})

func (s *MySuiteSim) TestHelloWorld(c *C) { //声明TestHelloWorld方法为MySuite套件的测试用例
	//c.Assert(42, Equals, "42")
	c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
	c.Check(42, Equals, 42)
}

func (s *MySuiteSim) Test_0191(c *C) {
	var x uint32 = 00000000000000000000000000001011
	c.Check(hammingWeight(x), Equals, 3)

}

//go test -v gocheck_test.go 191_number-of-1-bits.go
