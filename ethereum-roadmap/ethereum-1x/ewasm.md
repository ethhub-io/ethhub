# eWASM group

## Main unresolved questions
* Gas metering
* Memory allocation
* Interaction with the rest of EVM state (e.g. contract storage, balances)
* Interpreter/compiler guarantees on compilation time and runtime

## Gas metering
Two main approaches:
* Injection. Wasm bytecode gets pre-processed. An extra register is added to serve as a gas counter. It gets incremented at certain points (jumps, calls) and out-of-gas check is performed. Pro: generic. Con: performance overhead.
* Automatic upper bound estimation. Static analysis is performed on the bytecode, and, for some subset of codes, upper bound of executed instructions (virtual gas) can be calculated. Pro: no performance overhead. Con: only subset of codes

Current approach for the 1st phase (pre-compiles) is upper-bound based.

## Memory allocation
Wasm semantics dictates that Wasm execution has a linear memory (only one in the current version of the spec) that can be grown on demand.
Will that linear memory be allocated every time the engine is called, and then torn down at the end of the execution? If yes, how more efficient is this compared to the current EVM model (which does this allocation and tearing down at each CALL opcode).

## Interaction with the rest of EVM state
Was proposed via external functions, for example (name made up):

`function_SLOAD(storage_index: uint256)`

Alternative approach is not to have Ewasm code access EVM state, but only exchange input/output when called. This, of course, makes maintaining large persistent data structures difficult.

## Interpreter/compiler guarantees

Initially, this problem has been brought up in the context of JITs (Just In Time) compilers. JIT compilers were one of the reasons why WebAssembly was a big performance improvement over JavaScript.

JIT compilers might be problematic in an adversarial environment, because it is usually possible to find a program that takes an unusually long time to compile, and algorithms that decide what to compile “just in time” can be targeted too.

AOT (Ahead of Time) compilers can be used for Core Dev-controlled pre-compiles (Phase 1). For Phase 2, the plan was to initially use very straightforward interpreters, and then develop AOT compilers with necessary guarantees.
The idea of first introducing interpreters is to make sure eWASM is there, giving people more motivation to work on the compilers (which is harder than interpreter)
