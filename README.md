# CPython 3.7 ~ 3.11 Simple Speedtest
CPython 3.7 到 3.11 的简单测速。
* 本项目并非严格测试且已经搁置，主要目的是借此初步了解`pyperf`和`timeit`。
* Python3.11发布测试版不久，表现不俗，但已经发现很多性能问题。
## 环境
### CPython 版本
以下 CPython 从 python.org 下载64位可执行版本安装。
* Python 3.7.9
* Python 3.8.10
* Python 3.9.13
* Python 3.10.5
* Python 3.11.0b3
* PyPy 7.3.9 (Python 3.9.10)
* ~~numba / jax / Pyjion / diojit / pyston_v2~~
* ~~cython / nuitka~~
### 运行环境和疑问
* AMD Ryzen 9 5900HX with Radeon Graphics 3.30 GHz
* Windows 10 Pro 21H2 19044.1766
* 尽量减少系统负载。
## 测试方法和疑问
1. 在命令行调用 `pyperf timeit`。
```
py -{version} -m pyperf timeit [-s "{setup_code}"] "{run_code}" --rigorous
```
2. 在命令行调用 `timeit`。
3. 在命令行调用 `timeit -p`。
4. 在命令行运行脚本 `py a.py`调用函数50次，计算均值、标准差和极值。
5. 在 `PyCharm` 中用 CPython 以 `timeit` 调用函数50次，计算均值、标准差和极值。
6. 在 `PyCharm` 中用 CPython 以 `timeit -p` 调用函数50次，计算均值、标准差和极值。
7. 在 `PyCharm` 中用 CPython 运行脚本调用函数50次，用 `tiem.perf_counter` 取时间，计算均值、标准差和极值。

## 测试方法的疑问
* 函数调用 `timeit` 时返回值自动选择单位缩放数值，不改写的前提下如何获取时间单位？
* timeit 是否要`-p`？
* 垃圾回收 `gc.enable()` 是否要考虑？完整代码块？
* 部分版本有警告 `WARNING: unable to increase process priority`，是否影响结果？
* CMD的优先级是否影响结果？

## 测试小项
1. 全局变量 100M 单层空循环
2. 局部变量 100M 单层空循环
3. 局部变量 100M 单层循环赋值整数
4. 局部变量 10K x 10K 双层空循环
5. 生成 10K x 10K 二维数组，值全为0，无输出
6. 计算四个 [0, 100) 的某积
7. 计算 [0, 10M) 中各整数平方之和 (mod 1_000_000_007)
8. 无缓存计算 Fab(35)
9. ~~随机整数在集合中计数~~
10. 大整数集合in计算
11. 生成大列表
12. 大列表倒序
13. ~~随机大列表排序~~
14. 倒序大列表排序
15. 默认列表循环 pop(0)
16. ~~eval(随机整数和运算符拼接)~~

## 测试结果
1. 全局变量 100M 单层空循环
    * 其他语言简单测试：
      * `C`：29ms
      * `Java`（JIT）：1-2ms
      * `Java`（JIT，双层循环，外层重复数，内层 100M 次）：每次重复~30ms
      * `Java`（JIT，双层循环，外层 100M 次，内层重复数）：每次重复~300ms

| env | pyperf | timeit | timeit -p | py .py | py .py timeit | PyCharm .py | PyCharm .py timeit|
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7 | 1.90 ± 0.05 s | 1.91 s | 1.86 s | 1979.7 ± 77.8 ms<br>[1904.4, 2466.5] | 1952.0 ± 53.9 ms<br>[1878.3, 2108.2] | 2331.9 ± 27.4 ms<br>[2254.4, 2432.4] | 1888.8 ± 40.8 ms<br>[1828.7, 2009.7] |
| 3.8 | 1.96 ± 0.33 s<br>[?, 4.38] | 1.98 s | 1.86 s | 1894.2 ± 14.7 ms<br>[1865.6, 1928.0] | 1868.5 ± 5.5 s<br>[1860.0, 1886.2] | 1903.5 ± 65.9 ms<br>[1872.6, 2248.6] | 2117.9 ± 72.4 ms<br>[2077.0, 2579.1] |
| 3.9 | 1.74 ± 0.03 s | 1.83 s | 2.05 s | 1878.2 ± 72.1 ms<br>[1836.7, 2312.9] | 1872.6 ± 7.0 s<br>[1861.7, 1895.0] | 2239.1 ± 18.6 ms<br>[2.2056, 2.2761] | 2087.5 ± 26.6 ms<br>[2052.1, 2216.8] |
| 3.10 | 1.83 ± 0.07 s | 1.78 s |1.80 s | 1815.6 ± 11.9 ms<br>[1799.2, 1850.7] | 1817.0 ± 82.9 s<br>[1777.1, 2376.3] | 2020.9 ± 11.2 ms<br>[1987.9, 2049.6] | 1829.5 ± 72.0 ms<br>[1795.5, 2313.4] |
| 3.11 | 1.95 ± 0.04 s | 1.90 s | 2.00 s | 1996.5 ± 86.0 ms<br>[1961.4, 2587.4] | 1958.7 ± 20.7 s<br>[1930.8, 2052.5] | 1947.7 ± 62.2 ms<br>[1917.4, 2308.5] | 1937.0 ± 16.0 ms<br>[1908.7, 1979.3] |
| p3.9 | 1.04 ± 0.06 s<br>[?, 1.59] | 45.3 ± 0.024 ms | 45.5 ± 1.5 ms| 47.9 ± 6.0 ms<br>[45.2, 68.1] | 45.5± 1.4 ms<br>[44.6, 54.3] | 46.3 ± 1.4 ms<br>[45.3, 52.5]| 44.9 ± 0.6 s<br>[44.3, 47.4] |
pypy + pyperf/timeit 较复杂。

2. 局部变量 100M 单层空循环

| env | pyperf | timeit | timeit -p | py .py | py .py timeit| PyCharm | PyCharm timeit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7 | 1.15 ± 0.03 s| 1.09 s | 1.09 s | | | | |
| 3.8 | 938 ± 13 ms | 919 ms | 922 ms |||||
| 3.9 | 843 ± 37 ms | 846 ms | 828 ms |||||
| 3.10 | 910 ± 15 ms | 902 ms | 922 ms |||||
| 3.11 | 993 ± 20 ms| 1.03 s | 969 ms |||||
| p3.9 | 50.6 ± 3.3 ms| 46.1 ± 1.61 ms| 47.3 ± 2 ms |||||
## 参考
* [pyperf 文档](https://pyperf.readthedocs.io)
* [timeit 文档](https://docs.python.org/3/library/timeit.html)
* [timeit 心得](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module)
* [What’s New In Python 3.11](https://docs.python.org/3.11/whatsnew/3.11.html) ：Python 3.11 is up to 10-60% faster than Python 3.10. On average, we measured a 1.25x speedup on the standard benchmark suite. See Faster [CPython](https://docs.python.org/3.11/whatsnew/3.11.html#faster-cpython) for details.
* 2022年6月22日，我简单测试提交了[Py311的性能问题](https://github.com/faster-cpython/ideas/issues/420) ，2分钟后龟叔回复，一天内多位大佬参与后得出初步结论。
* 2022年6月30日，`阿-岳同学`发布[python3.11版速度性能优化了多少？](https://www.bilibili.com/video/BV1eT41137BH) 在 PyCharm中 对比了 Py311 和 Py37 的速度。
## 模板
| env | pyperf | PyCharm .py |
| --- | --- | --- |
| 3.7 |||
| 3.8 |||
| 3.9 |||
| 3.10 |||
| 3.11 |||
| p3.9 |||

| env | pyperf | timeit | timeit -p | py .py | py .py timeit | PyCharm | PyCharm timeit | PyCharm timeit -p |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.7 | ||||||||
| 3.8 | ||||||||
| 3.9 | ||||||||
| 3.10 |||||||||
| 3.11 |||||||||
| p3.9 |||||||||