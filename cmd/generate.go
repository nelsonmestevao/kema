/*
Copyright © 2021 Nelson Estevão <hello@estevao.org>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"os"
	"text/template"

	"github.com/spf13/cobra"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

type module struct {
	Name string
}

var generateCmd = &cobra.Command{
	Use:     "generate",
	Short:   "Generate a new module",
	Aliases: []string{"gen", "g"},
	Run: func(cmd *cobra.Command, args []string) {
		module := module{Name: "cena"}

		headerTemplate, err := template.ParseFiles("data/templates/header.tmpl.h")

		if err != nil {
			panic(err)
		}

		sourceTemplate, err := template.ParseFiles("data/templates/source.tmpl.c")

		if err != nil {
			panic(err)
		}

		header, err := os.Create(module.Name + ".h")
		source, err := os.Create(module.Name + ".c")

		check(headerTemplate.Execute(header, module))
		check(sourceTemplate.Execute(source, module))
	},
}

func init() {
	rootCmd.AddCommand(generateCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// generateCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// generateCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
