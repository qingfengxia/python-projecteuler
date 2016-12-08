#!/usr/bin/groovy

import groovy.util.GroovyTestCase;

/**  @brief
problem 352
weblink:  http://projecteuler.net/problem=352
description:

-----------------------------------------------------------------------------------------------

Each one of the 25 sheep in a flock must be tested for a rare virus, known to affect 2% of the sheep population. An accurate and extremely sensitive PCR test exists for blood samples, producing a clear positive / negative result, but it is very time-consuming and expensive.

Because of the high cost, the vet-in-charge suggests that instead of performing 25 separate tests, the following procedure can be used instead:

The sheep are split into 5 groups of 5 sheep in each group. For each group, the 5 samples are mixed together and a single test is performed. Then,

    If the result is negative, all the sheep in that group are deemed to be virus-free.
    If the result is positive, 5 additional tests will be performed (a separate test for each animal) to determine the affected individual(s).

Since the probability of infection for any specific animal is only 0.02, the first test (on the pooled samples) for each group will be:

    Negative (and no more tests needed) with probability 0.985 = 0.9039207968.
    Positive (5 additional tests needed) with probability 1 - 0.9039207968 = 0.0960792032.

Thus, the expected number of tests for each group is 1 + 0.0960792032 X 5 = 1.480396016.
Consequently, all 5 groups can be screened using an average of only 1.480396016 X 5 = 7.40198008 tests, which represents a huge saving of more than 70% !

Although the scheme we have just described seems to be very efficient, it can still be improved considerably (always assuming that the test is sufficiently sensitive and that there are no adverse effects caused by mixing different samples). E.g.:

    We may start by running a test on a mixture of all the 25 samples. It can be verified that in about 60.35% of the cases this test will be negative, thus no more tests will be needed. Further testing will only be required for the remaining 39.65% of the cases.
    If we know that at least one animal in a group of 5 is infected and the first 4 individual tests come out negative, there is no need to run a test on the fifth animal (we know that it must be infected).
    We can try a different number of groups / different number of animals in each group, adjusting those numbers at each level so that the total expected number of tests will be minimised.

To simplify the very wide range of possibilities, there is one restriction we place when devising the most cost-efficient testing scheme: whenever we start with a mixed sample, all the sheep contributing to that sample must be fully screened (i.e. a verdict of infected / virus-free must be reached for all of them) before we start examining any other animals.

For the current example, it turns out that the most cost-efficient testing scheme (we'll call it the optimal strategy) requires an average of just 4.155452 tests! (25 sheep)

Using the optimal strategy, let T(s,p) represent the average number of tests needed to screen a flock of s sheep for a virus having probability p to be present in any individual.
Thus, rounded to six decimal places, T(25, 0.02) = 4.155452 and T(25, 0.10) = 12.702124.

Find:  sum T(10000, p) for p=0.01, 0.02, 0.03, ... 0.50.
Give your answer rounded to six decimal places.

-------------------------------------------------------------------------------------------------------------
Analysis: 
    (1)BigDecimal has 16 significant digits, therefore there is no need to use BigDecimal class
    since integer part will not surpass 1000, 9 digits is enough to represent each T(n,p)
    groovy  float number default type is not double, but BigDecimal!!!
    
    (2) 5**2, square root is a good way, but for single group test, test on by one is not optimized!
    16=4*4 -> 4=2*2
    but most of value is not 
    
    (3) the grouping strategy may depends on the probability!  test p=0.01 0.1 0.5
     yes,  it is sensive to probability, if p=0.5, grouping test is not a good choice!
     in fact, p>0.39, grouping is not as effective as individual test!
    
    (4)
    100=2**2 * 5**2
    1000=2**3 * 5**3
    10000=2**4 * 5**4
    
    (5) when to do rounding is crucial!
    
    (6) This is dynamic programming,  after one test, the probability is changed!
    optimal measurement problems
    
*/
public class Projecteuler352 extends GroovyTestCase {

    BigDecimal round(BigDecimal r){
        //return  Math.round(r*10**6)/(10**6);   
        new BigDecimal(r).setScale(6, BigDecimal.ROUND_HALF_UP); 
        // round to 6 digits after the decimal point,
        // rounding can also be done by BigDecimal(double, digits)
    }



    /** @brief the general solution is hard to implemented, 
    but 1000 is speical number,  1000=2**3 * 5**3, thereby, only implement for n=1000!
    */
    BigDecimal leastTestFor10000( BigDecimal p){
        def r2=leastTestFor16(p)*leastTestFor625(1.0- (1.0-p)**16);
        def r3=leastTestFor625(p)*leastTestFor16(1.0- (1.0-p)**625);
        def r1=10000.0;
        return [r1,r2,r3].min();
    }

    BigDecimal leastTestFor2( BigDecimal p){
        def r1=2.0;
        def r2=singleGroupTest(2,p);
        return [r1,r2].min();
    }
    BigDecimal leastTestFor4( BigDecimal p){
        def r1=4.0;
        def r2=leastTestFor2(p)*leastTestFor2(1.0- (1.0-p)**2);
        def r3=singleGroupTest(4,p);
        return [r1,r2,r3].min();
    }
    BigDecimal leastTestFor8( BigDecimal p){
        //multiple tiers:  2X2X2
        def r1=8.0;  // one by one test!
        def r2=leastTestFor4(p)*leastTestFor2(1.0- (1.0-p)**4);
        def r3=leastTestFor2(p)*leastTestFor4(1.0- (1.0-p)**2);
        def r4=singleGroupTest(8,p);
        return [r1,r2,r3,r4].min();
    }
    BigDecimal leastTestFor16( BigDecimal p){
        //multiple tiers:  2X2X2X2  -> all factors  1, 2, 4, 8, 16
        def r1=16.0;  // one by one test!
        def r2=leastTestFor4(p)*leastTestFor4(1.0- (1.0-p)**4);
        def r3=leastTestFor8(p)*leastTestFor2(1.0- (1.0-p)**8);  
        def r4=leastTestFor2(p)*leastTestFor8(1.0- (1.0-p)**2);       
        def r5=singleGroupTest(16,p);
        return [r1,r2,r3,r4,r5].min();
    }

    BigDecimal leastTestFor5( BigDecimal p){
        def r1=5.0;
        def r2=singleGroupTest(5,p);
        return [r1,r2].min();
    }
    BigDecimal leastTestFor25( BigDecimal p){
        def r1=25.0;
        def r2=leastTestFor5(p)*leastTestFor5(1.0- (1.0-p)**5);
        def r3=singleGroupTest(25,p);
        println r1
        println r2
        println r3
        return [r1,r2,r3].min();
    }
    BigDecimal leastTestFor125( BigDecimal p){
        //multiple tiers:  5X5X5
        def r1=125.0;  // one by one test!
        def r2=leastTestFor25(p)*leastTestFor5(1.0- (1.0-p)**25);  // p need to be adjusted
        def r3=leastTestFor5(p)*leastTestFor25(1.0- (1.0-p)**5);  // p need to be adjusted
        def r4=singleGroupTest(125,p);
        return [r1,r2,r3,r4].min();
    }
    BigDecimal leastTestFor625( BigDecimal p){
        //multiple tiers:  5**n
        def r1=625.0;  // one by one test!
        def r2=leastTestFor25(p)*leastTestFor25(1.0- (1.0-p)**25);
        def r3=leastTestFor125( p)*leastTestFor5(1.0- (1.0-p)**125); 
        def r4=leastTestFor5( p)*leastTestFor125( 1.0- (1.0-p)**5);   
        def r5=singleGroupTest(625,p);
        return [r1,r2,r3,r4,r5].min();
    }

    //more genearal one,  list of factors with decreasing order
    BigDecimal leastTestForPowerN(int base, int power, BigDecimal p){
        //multiple tiers:  base=5, total=base**power, 
        if (power<=1)
            return [(double)base, singleGroupTest(base,p)].min();
        else
        {
            BigDecimal r1=singleGroupTest(base,p) *
                    leastTestForPowerN(base,  power-1,  1.0- (1.0-p)**base);
            //r2?
            return [r1,r2,r3].min();
        }
    }

    BigDecimal groupTest(int g, int n, BigDecimal p){
        def r=round(singleGroupTest(n,p)*singleGroupTest(g,1.0- (1.0-p)**n));
        if (r>g*n)  return g*n;
        else return r;
    }
    // n=1, it should return 1.0!
    BigDecimal singleGroupTest(int n , BigDecimal p){
        BigDecimal r=1.0;
        if (n>1) {
            r=1+ (1-(1.0-p)**n)*n;
            if (r>n)   r=n;
        }
        return r;
    }

    void test24(double prob)
    {
        println "test 24 is devided into groups:  3X8  4X6 2X12, p=${prob}, "
        def d=[1,2,3,4,6,8,12,24]
        int total=24;
        for(int i in d){
            BigDecimal r=groupTest((int)(total/i),i,prob)/total;
            println "Square GroupTest: groupCount=groupSize=${i}, testTimesRatio=${r}"
        }
    }

    void test25(double p)
    {
        for( int i in 1..25)         
        {
            //find the best single group size by calling 
            def r=round(singleGroupTest(i,p)/i)
            println "i=${i} and p=${p},  result=${r}"
            if (r>i) break;
        }
        println round(leastTestFor25(p) )    //failed!  leastTestFor24(0.1) +1.0
        println round(leastTestFor5(p) * 5 )  

        println "leastTestFor9(0.1) +leastTestFor16(0.1)=" 
        def result =leastTestFor8(p)*singleGroupTest(2,1.0- (1.0-p)**8) 
                             +singleGroupTest(3,p)*singleGroupTest(3,1.0- (1.0-p)**3)
        println round(result)  
    
    }
    /** @brief
    */
    //@test
    void test(){
    
        test25(0.1);
        //test24(0.02);

    
        /* println "basic function implementation test by assertion"
            //assert  groupTest(5,5,0.02) == 7.401980
            //assert singleGroupTest(5,0.02)==1.480396
            // this test must pass, before continue!
            //assert leastTestFor25(0.02)==4.155452
            //assert eastTestFor25(0.10) = 12.702124
            //assert singleGroupTest(1,0.02)==1.0
            println round(leastTestFor25(0.02))   //correctly
            */
        /*
        BigDecimal prob=0.02;
        println "test group size effect at  p=${prob} "
        for(int i in 2..10){
            BigDecimal r=groupTest(i,i,prob)/i/i;
            println "Square GroupTest: groupCount=groupSize=${i}, testTimesRatio=${r}"
        }
    
        println "probability sensitivy test for single group"
        def plist=[0.01, 0.05, 0.1, 0.5]
        for(BigDecimal p in plist){
            println "leastTestFor125 for p=${p} is:"+leastTestFor125(p).toString()
            println "leastTestFor125 for p=${p} is:"+leastTestFor125(p).toString()
        }

        for(int i in [2,4,8,5,25,125]){
            for(BigDecimal p in plist){
                def r=singleGroupTest(i,p)/i;
                println "single GroupTest for p=${p}, groupSize=${i}, testTimesRatio=${r}" 
            }
        }
        // even for p=0.5, the bigger the group, the less test times!
         */
    }

    //private fields
    BigDecimal start=0.01;
    BigDecimal step=0.01;
    BigDecimal end=0.50;
    //int count=1000;
    
    /* @brief test the correction by a small dimension first. 
     test  brute force first, method1,then, try some smart method! 
    */
    void bruteforce(){
        BigDecimal p=start;
        BigDecimal result=round(leastTestFor10000(p))
        println "for p=${p}, prob=${result}"
        while(p<=end){
            p+=step;
            def r=round(leastTestFor10000(p))
            println "for p=${p}, prob=${r}"
            result+=r;
        }
        println "result=${result}"
    }

    /** @brief
    */
    void smarter(){
    }
        
    /** @brief
    */
    void solve(){
        //bruteforce();
    }
        
    /** main() is not compulsory for groovy
    */
    public static void main(String[] args){
        Projecteuler352 p=new Projecteuler352();
        p.test();
        long start=System.nanoTime();
        p.solve();
        BigDecimal duration=(System.nanoTime() - start ) / 10.0**9;
        println("Solved in ${duration} seconds ")
    }
}

