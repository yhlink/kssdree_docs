Demonstrate the reference subtraction pipeline of Kssdtree on HG43 dataset, including a multi-step implementation and a one-step implementation.

# Multi-step implementation
```
import kssdtree

# step1、sketching a human reference genome (hg38) and 43 human genomes (HG43) with L3K10.shuf
kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='hg38.fa.gz', output='Ref_sketch', set_opt=True)
kssdtree.sketch(shuf_file='L3K10.shuf', genome_files='HG43', output='HG43_sketch', set_opt=True)

# step2、subtracting reference sketches (Ref_sketch) from input sketches (HG43_sketch)
kssdtree.subtract(ref_sketch='Ref_sketch', genome_sketch=='HG43_sketch', output=='HG43_sub_sketch')

# step3、calculating and creating distance matrix in phylip format required by NJ
kssdtree.dist(ref_sketch='HG43_sub_sketch', qry_sketch='HG43_sub_sketch', output='HG43.phylip', flag=0)

# step4、constructing tree with NJ
kssdtree.build(phylip='HG43.phylip', output='HG43.newick', method='nj')

# step5、visualizing tree 
kssdtree.visualize(newick='HG43.newick', taxonomy='HG43.txt', mode='r')
# Note: HG43.txt records names (accessions) and taxonomies of 43 human genomes.

```

# One-step implementation (Recommendation)
```
import kssdtree

kssdtree.quick(shuf_file='L3K10.shuf', genome_files='HG43', output='HG43.newick', reference='hg38.fa.gz', taxonomy='HG43.txt', method='nj', mode='r')
```
