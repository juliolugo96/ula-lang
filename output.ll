; ModuleID = "/home/ignisgravitas/semester/compiladores/ula_lang/code_gen/codegen.py"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = mul i8 4, 4
  %".3" = add i8 %".2", 2
  store i8 %".3", i8* @"x"
  %".5" = load i8, i8* @"x"
  %".6" = icmp eq i8 %".5", 17
  br i1 %".6", label %"entry.if", label %"entry.else"
entry.if:
  store i8 3, i8* @"x"
  br label %"entry.endif"
entry.else:
  store i8 1, i8* @"x"
  br label %"entry.endif"
entry.endif:
  %".12" = load i8, i8* @"x"
  %".13" = bitcast [5 x i8]* @"fstr" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8 %".12")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"read"(i8* %".1", ...) 

@"x" = global i8 0
@"fstr" = internal constant [5 x i8] c"%i \0a\00"