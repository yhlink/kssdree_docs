def shuffle(k=None, s=None, l=None, o=None):
    """

       Generating .shuf file.

       Args:
           k (int): Half-length of k-mer, k=x meaning use k-mer of length 2x.
           s (int): Half-length of k-mer substring, s=x meaning the whole space is the collection of all 2x-mer. Make sure l < s < k. The default setting is -s 6, usually there is no need to change this setting.
           l (int): The level of dimensionality-reduction. l=x meaning the expected rate of dimensionality-reduction is 16^x.
           o (str): The output filename of .shuf file.

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def sketch(shuf_file=None, genomes_file=None, output=None, set_opt=None):
    """

           Sketching genomes into sketch and generating sketch files.

           Args:
               shuf_file (str): The path of .shuf file. Kssdtree provide multiple .shuf files ('L3K9.shuf', 'L3K10.shuf', etc.) as input for genome decomposition. The default is 'L3K10.shuf'.
               genomes_file (str): The folder path for genome files. Kssdtree supports the input of genome files in both fasta and fastq formats.
               output (str): The output folder path for sketch result files of genome files.
               set_opt (bool): Perform set operations (subtract and retrieve) if needed, default is False. To perform set operations, set set_opt=True.

           Return:
               bool: True

           Example:
                >>> kssdtree.sketch(shuf_file='L3K10.shuf', genomes_file='ES29', output='ES29_sketch')
                True
                >>> kssdtree.sketch(shuf_file='../shuf_file/L3K10.shuf', genomes_file='../data/ES29', output='ES29_sketch')
                True

    """
    return True


def dist(ref_sketch=None, qry_sketch=None, output=None, flag=None):
    """

       Generating .shuf file.

       Args:
           ref_sketch (str):
           qry_sketch (str):
           output (str):
           flag (int):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def retrieve(ref_sketch=None, qry_sketch=None, output=None, N=None):
    """

       Generating .shuf file.

       Args:
           ref_sketch (str):
           qry_sketch (str):
           output (str):
           N (int):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def build(phylip=None, output=None, method=None):
    """

       Generating .shuf file.

       Args:
           phylip (str):
           output (str):
           method (str):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def visualize(newick=None, taxonomy=None, mode=None):
    """

       Generating .shuf file.

       Args:
           newick (str):
           taxonomy (str):
           mode (str):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def subtract(ref_sketch=None, genomes_sketch=None, output=None, flag=None):
    """

       Generating .shuf file.

       Args:
           ref_sketch (str):
           genomes_sketch (str):
           output (str):
           flag (int):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True


def quick(shuf_file=None, genomes_file=None, output=None, reference=None, taxonomy=None, method=None, mode=None, N=None):
    """

       Generating .shuf file.

       Args:
           shuf_file (str):
           genomes_file (str):
           output (str):
           reference (str):
           taxonomy (str):
           method (str):
           mode (str)
           N (int):

       Return:
           bool: True

       Example:
            >>> kssdtree.shuffle(k=10, s=6, l=3, o='L3K10.shuf')
            True

    """
    return True
