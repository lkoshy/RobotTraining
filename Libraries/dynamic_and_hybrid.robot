*** Settings ***
Library     DynamicLibrary.py
Library     HybridLibrary.py

*** Test Cases ***
Dynamic example
    Dynamic keyword
    Keyword with arguments      foo
    Keyword with arguments      bar
    Keyword with arguments      foo  arg3=bar

Hybrid example
    Hybrid keyword
    External hybrid keyword     argh
