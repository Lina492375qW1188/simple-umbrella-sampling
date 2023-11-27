# simple-umbrella-sampling

1-dim example umbrella sampling and the corresponding Weighted Histogram Analysis Method (WHAM) demonstration in python.
The references and explanation will be updated soon.

```
cd wham
wham clean
make wham
```
Before compile using make, remember to change to reduced unit defined in `wham/wham.h`.

(There is a `job.sh` file in wham/wham/ )
```
./wham -1.5 1.5 15 0.01 1 0 metadata freefile_bin[number_of_bins]
```
