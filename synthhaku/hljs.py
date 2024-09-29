# -*- coding: utf-8 -*-

"""
synthhaku.hljs
~~~~~~~~~~~~

Constants and functions related to syntax highlighting with highlight.js

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import re
import typing

__all__ = ("get_language", "guess_file_traits", "LANGUAGES")


LANGUAGES = sorted(
    [
        "as",
        "1c",
        "abnf",
        "accesslog",
        "actionscript",
        "ada",
        "ado",
        "adoc",
        "apache",
        "apacheconf",
        "applescript",
        "arduino",
        "arm",
        "armasm",
        "asciidoc",
        "aspectj",
        "atom",
        "autohotkey",
        "autoit",
        "avrasm",
        "awk",
        "axapta",
        "bash",
        "basic",
        "bat",
        "bf",
        "bind",
        "bnf",
        "brainfuck",
        "c",
        "c++",
        "cal",
        "capnp",
        "capnproto",
        "cc",
        "ceylon",
        "clean",
        "clj",
        "clojure-repl",
        "clojure",
        "cls",
        "cmake.in",
        "cmake",
        "cmd",
        "coffee",
        "coffeescript",
        "console",
        "coq",
        "cos",
        "cpp",
        "cr",
        "craftcms",
        "crm",
        "crmsh",
        "crystal",
        "cs",
        "csharp",
        "cson",
        "csp",
        "css",
        "d",
        "dart",
        "dcl",
        "delphi",
        "dfm",
        "diff",
        "django",
        "dns",
        "do",
        "docker",
        "dockerfile",
        "dos",
        "dpr",
        "dsconfig",
        "dst",
        "dts",
        "dust",
        "ebnf",
        "elixir",
        "elm",
        "erb",
        "erl",
        "erlang-repl",
        "erlang",
        "excel",
        "f90",
        "f95",
        "feature",
        "fix",
        "flix",
        "fortran",
        "freepascal",
        "fs",
        "fsharp",
        "gams",
        "gauss",
        "gcode",
        "gemspec",
        "gherkin",
        "glsl",
        "gms",
        "go",
        "golang",
        "golo",
        "gradle",
        "graph",
        "groovy",
        "gss",
        "gyp",
        "h",
        "h++",
        "haml",
        "handlebars",
        "haskell",
        "haxe",
        "hbs",
        "hpp",
        "hs",
        "hsp",
        "html.handlebars",
        "html.hbs",
        "html",
        "htmlbars",
        "http",
        "https",
        "hx",
        "hy",
        "hylang",
        "i7",
        "iced",
        "icl",
        "inform7",
        "ini",
        "instances",
        "irb",
        "irpf90",
        "java",
        "javascript",
        "jboss-cli",
        "jinja",
        "js",
        "json",
        "jsp",
        "jsx",
        "julia",
        "k",
        "kdb",
        "kotlin",
        "lasso",
        "lassoscript",
        "lazarus",
        "ldif",
        "leaf",
        "less",
        "lfm",
        "lisp",
        "livecodeserver",
        "livescript",
        "llvm",
        "lpr",
        "ls",
        "lsl",
        "lua",
        "m",
        "mak",
        "makefile",
        "markdown",
        "mathematica",
        "matlab",
        "maxima",
        "md",
        "mel",
        "mercury",
        "mips",
        "mipsasm",
        "mizar",
        "mk",
        "mkd",
        "mkdown",
        "ml",
        "mm",
        "mma",
        "mojolicious",
        "monkey",
        "moo",
        "moon",
        "moonscript",
        "n1ql",
        "nc",
        "nginx",
        "nginxconf",
        "nim",
        "nimrod",
        "nix",
        "nixos",
        "nsis",
        "obj-c",
        "objc",
        "objectivec",
        "ocaml",
        "openscad",
        "osascript",
        "oxygene",
        "p21",
        "parser3",
        "pas",
        "pascal",
        "patch",
        "pb",
        "pbi",
        "pcmk",
        "perl",
        "pf.conf",
        "pf",
        "php",
        "php3",
        "php4",
        "php5",
        "php6",
        "pl",
        "plist",
        "pm",
        "podspec",
        "pony",
        "powershell",
        "pp",
        "processing",
        "profile",
        "prolog",
        "protobuf",
        "ps",
        "puppet",
        "purebasic",
        "py",
        "python",
        "q",
        "qml",
        "qt",
        "r",
        "rb",
        "rib",
        "roboconf",
        "rs",
        "rsl",
        "rss",
        "ruby",
        "ruleslanguage",
        "rust",
        "scad",
        "scala",
        "scheme",
        "sci",
        "scilab",
        "scss",
        "sh",
        "shell",
        "smali",
        "smalltalk",
        "sml",
        "sqf",
        "sql",
        "st",
        "stan",
        "stata",
        "step",
        "step21",
        "stp",
        "styl",
        "stylus",
        "subunit",
        "sv",
        "svh",
        "swift",
        "taggerscript",
        "tao",
        "tap",
        "tcl",
        "tex",
        "thor",
        "thrift",
        "tk",
        "toml",
        "tp",
        "ts",
        "twig",
        "typescript",
        "v",
        "vala",
        "vb",
        "vbnet",
        "vbs",
        "vbscript-html",
        "vbscript",
        "verilog",
        "vhdl",
        "vim",
        "wildfly-cli",
        "x86asm",
        "xhtml",
        "xjb",
        "xl",
        "xls",
        "xlsx",
        "xml",
        "xpath",
        "xq",
        "xquery",
        "xsd",
        "xsl",
        "yaml",
        "yml",
        "zep",
        "zephir",
        "zone",
        "zsh",
    ],
    key=len,
    reverse=True,
)


def get_language(query: str) -> str:
    """Tries to work out the highlight.js language of a given file name or
    shebang. Returns an empty string if none match.
    """
    query = query.lower()
    for language in LANGUAGES:
        if query.endswith(language):
            return language
    return ""


ENCODING_REGEX = re.compile(rb"coding[=:]\s*([-\w.]+)")


def guess_file_traits(data: bytes) -> typing.Tuple[str, str, typing.Optional[str]]:
    """
    Given the content of a file, attempts to guess its encoding and language.

    Returns as a tuple of (content, encoding, language),
    where language may be None.

    Raises UnicodeDecodeError if the encoding cannot be guessed.
    """

    try:
        content = data.decode("utf-8")
        encoding = "utf-8"
    except UnicodeDecodeError as exc:
        # This file isn't UTF-8.

        #  By Python and text-editor convention,
        # there may be a hint as to what the actual encoding is
        # near the start of the file.

        encoding_match = ENCODING_REGEX.search(data[:128])

        if encoding_match:
            encoding = encoding_match.group(1)
        else:
            raise exc

        try:
            encoding = encoding.decode("utf-8")
            content = data.decode(encoding)
        except UnicodeDecodeError as exc2:
            raise exc2 from exc

    language = None

    if content.startswith("#!") and "\n" in content:
        language = get_language(content[: content.find("\n")]) or language

    return content, encoding, language
