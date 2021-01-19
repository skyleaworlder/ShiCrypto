# DEPENDENCY

由于本项目有写个 `GUI` 的打算，所以要总结一下依赖和接口。

在分析了一个小时的技术可行性之后，觉得可以参考著名开源项目 `CTFCrackTool` 的想法，使用 `Jython` 给所有的脚本 “套个壳”，然后用 `swing` 来做 `GUI`。

但目前还没有任何想法。仅仅是想更优化项目结构，让其更合理，更容易上手和了解（以及我个人的进一步分析）。为此有该 `md` 文件。

|名称|所使用库|
|-|-|
|Calcu|sys|
|ConMod|sys|
|continued|sys|
|CRT|sys, functools:reduce(waiting...)|
|ECC|sys, **numpy(todo: rm)**, math|
|ECIES|sys, random|
|ELGamal|sys, random|
|IntFactorize|sys, math, functool:reduce(waiting...)|
|Morse|sys, functool:reduce(waiting...)|
|MultCoef|sys, functool:reduce(waiting...), math|
|Pohlig-Hellman|sys|
|Pollard-Rho-Log|sys, math|
|PrimeTest|sys, random, **sympy(todo: rm)**, math|
|QuadResidue|sys, math, functool:reduce(waiting...)|
|RSA|sys, **sympy(todo: rm)**, random|
|Shanks|sys, math|
