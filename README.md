
<!DOCTYPE html><html><head><meta charset="utf-8">
</head><body id="preview">
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Python_Prime_Library_0"></a>Python Prime Library</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">This official documentation of python prime library.</p>
<ul>
<li class="has-line-data" data-line-start="4" data-line-end="5">Generate Specific type of Prime numbers between given range</li>
<li class="has-line-data" data-line-start="5" data-line-end="6">Generate Random Prime number</li>
<li class="has-line-data" data-line-start="6" data-line-end="8">Factorization of given number</li>
</ul>
<h1 class="code-line" data-line-start=8 data-line-end=9 ><a id="Installation_8"></a>Installation!</h1>
<pre> Use<b> pip3</b> if you are using python version 3+ else follow same steps as mentioned below</pre>
<ol>
<li class="has-line-data" data-line-start="9" data-line-end="10">If you don’t have pip then follow below procedure else go to step 2.</li>
</ol>
<ul>
<li class="has-line-data" data-line-start="10" data-line-end="18">For window Users
<ul>
<li class="has-line-data" data-line-start="11" data-line-end="12">Download <a href="https://bootstrap.pypa.io/get-pip.py">get-pip</a> to a folder on your computer.</li>
<li class="has-line-data" data-line-start="12" data-line-end="13">Put that file on Desktop</li>
<li class="has-line-data" data-line-start="13" data-line-end="18">Open cmd and run the following commands:<pre><code class="has-line-data" data-line-start="15" data-line-end="18" class="language-sh">$ <span class="hljs-built_in">cd</span> Desktop
$ python get-pip.py
</code></pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="18" data-line-end="27">For Mac Users
<ul>
<li class="has-line-data" data-line-start="19" data-line-end="23">Install python<pre><code class="has-line-data" data-line-start="21" data-line-end="23" class="language-sh">$ brew install python
</code></pre>
</li>
<li class="has-line-data" data-line-start="23" data-line-end="27">Run the following command:<pre><code class="has-line-data" data-line-start="25" data-line-end="27" class="language-sh">$ python get-pip.py
</code></pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="27" data-line-end="46">For Linux Users
<ul>
<li class="has-line-data" data-line-start="28" data-line-end="38">Run the following commands for python(version &gt; 2.0):<pre><code class="has-line-data" data-line-start="30" data-line-end="38" class="language-sh">$ sudo apt-get install python-pip
$ sudo pacman -S python2-pip
$ sudo yum upgrade python-setuptools
$ sudo yum install python-pip python-wheel
$ sudo dnf upgrade python-setuptools
$ sudo dnf install python-pip python-wheel
$ sudo zypper install python-pip python-setupt ools python-wheel
</code></pre>
</li>
<li class="has-line-data" data-line-start="38" data-line-end="46">Run the following commands for python(version &gt; 3.0):<pre><code class="has-line-data" data-line-start="40" data-line-end="46" class="language-sh">$ sudo apt-get install python3-pip
$ sudo pacman -S python-pip
$ sudo yum install python3 python3-wheel
$ sudo dnf install python3 python3-wheel
$ sudo zypper install python3-pip python3-setu ptools python3-wheel
</code></pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="46" data-line-end="55">For Raspberry Users
<ul>
<li class="has-line-data" data-line-start="47" data-line-end="51">Run the following commands for python(version &gt; 2.0):<pre><code class="has-line-data" data-line-start="49" data-line-end="51" class="language-sh">$ sudo apt-get install python-pip
</code></pre>
</li>
<li class="has-line-data" data-line-start="51" data-line-end="55">Run the following commands for python(version &gt; 2.0):<pre><code class="has-line-data" data-line-start="53" data-line-end="55" class="language-sh">$ sudo apt-get install python3-pip
</code></pre>
</li>
</ul>
</li>
</ul>
<ol start="2">
<li class="has-line-data" data-line-start="55" data-line-end="61">Import gmpy2 file
<ul>
<li class="has-line-data" data-line-start="56" data-line-end="57">This package is require to install primelibpy library</li>
<li class="has-line-data" data-line-start="57" data-line-end="61">Run following command<pre><code class="has-line-data" data-line-start="59" data-line-end="61" class="language-sh">$ pip install gmpy2==<span class="hljs-number">2.1</span>.<span class="hljs-number">0</span>a2
</code>
<pre>OR if you are using Python 3</pre>
<code class="has-line-data" data-line-start="59" data-line-end="61" class="language-sh">$ pip3 install gmpy2==<span class="hljs-number">2.1</span>.<span class="hljs-number">0</span>a2
</code>
</pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="61" data-line-end="67">Now, install prime python library using below command.
<ul>
<li class="has-line-data" data-line-start="62" data-line-end="67">Run following command<pre><code class="has-line-data" data-line-start="64" data-line-end="66" class="language-sh">$ pip install primelibpy
</code></pre>
</li>
</ul>
</li>
</ol>
<h1 class="code-line" data-line-start=67 data-line-end=68 ><a id="Functions_Description_67"></a>Functions Description</h1>
<ul>
<li class="has-line-data" data-line-start="69" data-line-end="70">
<h3 class="code-line" data-line-start=69 data-line-end=70 ><a id="Prime_Functions_69"></a>Prime Functions</h3>
</li>
</ul>
<p class="has-line-data" data-line-start="70" data-line-end="71">In all the prime numbers Start_Limit and End_Limit are the range of prime number user wants to print inclusively.</p>
<h4 class="code-line" data-line-start=71 data-line-end=72 ><a id="Balanced_Prime_71"></a>Balanced Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="72" data-line-end="75">Syntex: <code>getBalancedPrime(startLimit,endLimit,balancedMode)</code><br>
Return Type: <code>list</code><br>
Description: Balanced_Mode is how number which decide balanced limit for prime.</p>
</blockquote>
<h4 class="code-line" data-line-start=76 data-line-end=77 ><a id="Circular_Prime_76"></a>Circular Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="77" data-line-end="79">Syntex: <code>getCircularPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=80 data-line-end=81 ><a id="Cousin_Prime_80"></a>Cousin Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="81" data-line-end="84">Syntex: <code>getCousinPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code><br>
Description: Cousin prime are in pair so return list is have list inside it e.g.[ [1,2], [2,3] ]</p>
</blockquote>
<h4 class="code-line" data-line-start=85 data-line-end=86 ><a id="Double_Mersenne_Prime_85"></a>Double Mersenne Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="86" data-line-end="88">Syntex: <code>getDoubleMersennePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=89 data-line-end=90 ><a id="Factorial_Prime_89"></a>Factorial Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="90" data-line-end="92">Syntex: <code>getFactorialPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=93 data-line-end=94 ><a id="Good_Prime_93"></a>Good Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="94" data-line-end="96">Syntex: <code>getGoodPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=97 data-line-end=98 ><a id="Mersenne_Prime_97"></a>Mersenne Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="98" data-line-end="100">Syntex: <code>getMersennePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=101 data-line-end=102 ><a id="Palindromic_Prime_101"></a>Palindromic Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="102" data-line-end="104">Syntex: <code>getPalindromicPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=105 data-line-end=106 ><a id="Permutable_Prime_105"></a>Permutable Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="106" data-line-end="108">Syntex: <code>getPermutablePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=109 data-line-end=110 ><a id="Primorial_Prime_109"></a>Primorial Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="110" data-line-end="112">Syntex: <code>getPrimorialPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=113 data-line-end=114 ><a id="Fermat_Pseudo_Prime_113"></a>Fermat Pseudo Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="114" data-line-end="117">Syntex: <code>getFermatPseudoPrime(baseNumber,noPsedoPrime)</code><br>
Return Type: <code>list</code><br>
Description: Base_number is halp to generate composite number ,and second argument is Total number of Pseudo primes</p>
</blockquote>
<h4 class="code-line" data-line-start=118 data-line-end=119 ><a id="Pythagorean_Prime_118"></a>Pythagorean Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="119" data-line-end="121">Syntex: <code>getPythagoreanPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=122 data-line-end=123 ><a id="Reversible_Prime_122"></a>Reversible Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="123" data-line-end="125">Syntex: <code>getReversiblePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=126 data-line-end=127 ><a id="Semi_Prime_126"></a>Semi Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="127" data-line-end="129">Syntex: <code>getSemiPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=130 data-line-end=131 ><a id="Sophie_Germain_Prime_130"></a>Sophie Germain Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="131" data-line-end="133">Syntex: <code>getSophieGermainPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=134 data-line-end=135 ><a id="Twin_Prime_134"></a>Twin Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="135" data-line-end="138">Syntex: <code>getTwinPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code><br>
Description: Twin prime are in pair so return list is have list inside it e.g.[ [1,2], [2,3] ]</p>
</blockquote>
<h4 class="code-line" data-line-start=139 data-line-end=140 ><a id="Wagstaff_Prime_139"></a>Wagstaff Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="140" data-line-end="142">Syntex: <code>getWagstaffPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=143 data-line-end=144 ><a id="Wieferich_Prime_143"></a>Wieferich Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="144" data-line-end="146">Syntex: <code>getWieferichPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=147 data-line-end=148 ><a id="Wilson_Prime_147"></a>Wilson Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="148" data-line-end="150">Syntex:<code>getWilsonPrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=151 data-line-end=152 ><a id="Left_Truncatable_Prime_151"></a>Left Truncatable Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="152" data-line-end="154">Syntex: <code>getLeftTruncatablePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=155 data-line-end=156 ><a id="Right_Truncatable_Prime_155"></a>Right Truncatable Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="156" data-line-end="158">Syntex: <code>getRightTruncatablePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=159 data-line-end=160 ><a id="Truncatable_Prime_159"></a>Truncatable Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="160" data-line-end="162">Syntex: <code>getTruncatablePrime(startLimit,endLimit)</code><br>
Return Type: <code>list</code></p>
</blockquote>
<h4 class="code-line" data-line-start=163 data-line-end=164 ><a id="Gaussian_Prime_163"></a>Gaussian Prime</h4>
<blockquote>
<p class="has-line-data" data-line-start="164" data-line-end="166">Syntex: <code>getGaussianPrime(startLimit,endLimit)</code><br>
Return Type: <code>None</code></p>
</blockquote>
<ul>
<li class="has-line-data" data-line-start="167" data-line-end="169">
<h3 class="code-line" data-line-start=167 data-line-end=168 ><a id="Factorization_167"></a>Factorization</h3>
</li>
</ul>
<p class="has-line-data" data-line-start="70" data-line-end="71">This Section is realted to  Number factorization. Use Semi-Prime where it is indicated. </p>
<h4 class="code-line" data-line-start=169 data-line-end=170 ><a id="Traditional_Way_for_Factorization_169"></a>Traditional Way for Factorization</h4>
<blockquote>
<p class="has-line-data" data-line-start="170" data-line-end="172">Syntex: <code>getFactorTraditional(semiPrimeNumber)</code><br>
Return Type: <code>list</code><br>
Note: This function will work all kind of number but I'll suggest to use Semi prime number because This funciton returns Factor of input number except 1 and number itself.
</p>
</blockquote>
<h4 class="code-line" data-line-start=173 data-line-end=174 ><a id="Fermat_Theorem_for_Factorization_173"></a>Fermat Theorem for Factorization</h4>
<blockquote>
<p class="has-line-data" data-line-start="174" data-line-end="177">Syntex: <code>getFactorFermatTheorem(semiPrimeNumber)</code><br>
Return Type: <code>tuple</code><br>
Note: This is only for composite number who have only two prime factors except number itself e.g. 33 have two prime factors 3 and 11.</p>
</blockquote>
<h4 class="code-line" data-line-start=178 data-line-end=179 ><a id="Pollard_Rho_for_Factorization_178"></a>Pollard Rho for Factorization</h4>
<blockquote>
<p class="has-line-data" data-line-start="179" data-line-end="182">Syntex: <code>getFactorPollardRho(semiPrimeNumber)</code><br>
Return Type: <code>integer</code><br>
Note: This will return any one factor of given number because this algorithem works on random numbers.</p>
</blockquote>
<h4 class="code-line" data-line-start=178 data-line-end=179 ><a id="Pollard_Rho_for_Factorization_178"></a>General Factorization</h4>
<blockquote>
<p class="has-line-data" data-line-start="179" data-line-end="182">Syntex: <code>getAllFactors(compositeNumber)</code><br>
Return Type: <code>list</code><br>
Note: This will return list of all prime factors.</p>
</blockquote>
<h2 class="code-line" data-line-start=183 data-line-end=185 ><a id="License_183"></a>License</h2>
<p class="has-line-data" data-line-start="186" data-line-end="188">MIT<br>
<p class="has-line-data" data-line-start="189" data-line-end="190"><strong>Free Software, Hell Yeah!</strong></p>
<p class="has-line-data" data-line-start="191" data-line-end="192">Follow me on</p>
<div class="row" >
    <a href="https://github.com/mit1280"><img src="http://ist.mit.edu/sites/default/files/styles/news_image_node/public/news_images/github_silhouette-740x555.jpg" alt="Image of Yaktocat" width="130" height="100" style="padding: 20px" ></a>
    <a href="https://www.linkedin.com/in/mitpatel12/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Linkedin.svg/1200px-Linkedin.svg.png" alt="Image of Yaktocat" width="100" height="100" style="padding: 20px"></a>
    <a href="https://www.facebook.com/patel.mit.37"><img src="https://en.facebookbrand.com/wp-content/uploads/2019/04/f_logo_RGB-Hex-Blue_512.png" alt="Image of Yaktocat" width="100" height="100" style="padding: 20px"></a>      
    <a href="https://www.instagram.com/mit_0812/"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-instagram-new-circle-512.png" alt="Image of Yaktocat" width="100" height="100" style="padding: 20px"></a>    
</div>
</body></html>

