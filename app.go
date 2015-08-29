package main

import (
    "github.com/go-martini/martini"
    "github.com/martini-contrib/render"
    )

func main() {
  m := martini.Classic()
  m.Use(martini.Static("assets"))
  m.Use(render.Renderer(render.Options{
      Directory: "templates",
      Extensions: []string{".html"},
      Charset: "utf-8",
  }))
  m.Get("/", func(r render.Render) {
     r.HTML(200, "index", "")
   })
  m.Run()
}
