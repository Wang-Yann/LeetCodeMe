package main


import (
	"testing"
	"io"
	"fmt"
	"strconv"
	. "gopkg.in/check.v1"

)

var a int =1

// Hook up gocheck into the "go test" runner.
func Test(t *testing.T) { TestingT(t) }

type MySuite struct{}

var _ = Suite(&MySuite{})


func (s *MySuite) SetUpSuite(c *C) {
	str3:="第1次套件开始执行"
	fmt.Println(str3)

}

func (s *MySuite) TearDownSuite(c *C) {
	str4:="第1次套件执行完成"
	fmt.Println(str4)
}

func (s *MySuite) SetUpTest(c *C) {
	str1:="第"+strconv.Itoa(a)+"条用例开始执行"
	fmt.Println(str1)

}

func (s *MySuite) TearDownTest(c *C) {
	str2:="第"+strconv.Itoa(a)+"条用例执行完成"
	fmt.Println(str2)
	a=a+1
}

func (s *MySuite) TestHelloWorld(c *C) {
	c.Assert(42, Equals, 42)
	c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
	c.Check(42, Equals, 42)
}

func (s *MySuite) TestHelloTerry(c *C) {
	c.Assert("terry", Equals, "terry")
	c.Assert(io.ErrClosedPipe, ErrorMatches, "io: .*on closed pipe")
	c.Check(42, Equals, 42)
}
