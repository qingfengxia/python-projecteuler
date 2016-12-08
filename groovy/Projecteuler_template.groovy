#!/usr/bin/groovy

/*
 java.math.BigDecimal and BigInteger have been imported by groovy
 This template is mainly for groovy, but coding is compatible with java except println()
 */
     
//package net.projecteuler;

/** @brief

problem ???
weblink:
description:
----------------------------------------------------------

---------------------------------------------------------
Analysis:

*/
public class Projecteuler???{
    /** @brief
    */
    void test(){
        //assert 
    }

    /** @brief
     test the correction by a small dimension first. 
     test  brute force first, method1,then, try some smart method! 
    */
    void bruteforce(){

    }
    /** @brief
    */
    void smarter(){
    }
        
    /** @brief
    */
    void solve(){
        bruteforce();
    }
        
    /** main() is not compulsory for groovy
    */
    public static void main(String[] args){
        Projecteuler??? p=new Projecteuler???();
        p.test();
        long start=System.nanoTime();
        p.solve();
        double duration=(System.nanoTime() - start ) / 10.0**9;
        println "Solved in ${duration} seconds "
    }
}
