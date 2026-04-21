# CS154 Lab3 Test Utility <hr>

The directory structure to run this should look like:
```
.
├── tests/
│   ├── factorial_test.s
|   ├── slt_test.s
│   └── any_other_tests.s ...
|
├── mips_to_hex.sh
|
├── i_mem_text_init.txt
|
├── test.py
|
└── ucsbcs154lab4_cpu.py
```

Make sure somewhere in your `ucsbcs154lab4_cpu.py` you define the following `test()` function:

```
def test():
   sim_trace = pyrtl.SimulationTrace()

    # Initialize the i_mem with your instructions.
   i_mem_init = {}
   with open('i_mem_init.txt', 'r') as fin:
        i = 0
        for line in fin.readlines():
            i_mem_init[i] = int(line, 16)
            i += 1

   sim = pyrtl.Simulation(tracer=sim_trace, memory_value_map={
        i_mem : i_mem_init
    })

    # Run for an arbitrarily large number of cycles.

   for cycle in range(100):
        sim.step({})
      
   return (
      sim.inspect_mem(d_mem),
      sim.inspect_mem(rf),
   )
```
This allows the `test.py` file to retrieve the outputs of the CPU in dictionary forms.
When I submitted the CPU file I commented this out in case the gradescope tests will get mad at the definition.

Any added test files should have an answer section formatted like so:
```
# ANSWER
# mem[0] = 1
# $t1 = 2
```

Then just run `python test.py` and it should loop through the `tests` directory and check each test inside. I ran this on CSIL.

Note: The factorial test uses tabs to separate the factorial clarification comment.

You can change the whitespace the parser searches for by modifying line 45 in `test.py`.
