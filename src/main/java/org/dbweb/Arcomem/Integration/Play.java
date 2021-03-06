package org.dbweb.Arcomem.Integration;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

import org.dbweb.socialsearch.shared.Params;
import org.dbweb.socialsearch.topktrust.algorithm.TopKAlgorithm;
import org.dbweb.socialsearch.topktrust.algorithm.functions.PathMultiplication;
import org.dbweb.socialsearch.topktrust.algorithm.paths.OptimalPaths;
import org.dbweb.socialsearch.topktrust.algorithm.score.Score;
import org.dbweb.socialsearch.topktrust.algorithm.score.TfIdfScore;

public class Play {

  private static final int N_EXPERIMENTS = 1;

  public static void main(String[] args) {
    Params.dir = "/home/lagree/git/TOPKS/test/yelp/TOPZIP/small/";
    Params.networkFile = "network.txt";
    Params.triplesFile = "triples.txt";
    // Index files and load data in memory
    Score score = new TfIdfScore();
    OptimalPaths optpath = new OptimalPaths("network", true);
    TopKAlgorithm algo = new TopKAlgorithm(score, 0f, new PathMultiplication(), optpath);
    List<String> query = new ArrayList<String>();
    //query.add("stand");
    //Params.DISK_BUDGET = 400;
    //algo.executeTOPKSMBaselineQuery(29643, query, 5, 0.001f, 30000, 100000);
    PrintWriter writer;
    try {
      writer = new PrintWriter("ndcg.csv", "UTF-8");
      long before = System.currentTimeMillis();
      int c = 0;
      for (int seeker: algo.getUsers().keySet().toArray()) {
        Map<Integer, Float> ndcgDistribution = algo.userSequenceDistribution(seeker);
        writer.print(seeker+"#");
        for (int u: ndcgDistribution.keySet())
          writer.print(u+":"+ndcgDistribution.get(u)+";");
        writer.print("\n");
        c += 1;
      }
      System.out.println((System.currentTimeMillis() - before) / 1000 + "s");
      writer.close();
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (UnsupportedEncodingException e) {
      e.printStackTrace();
    }
    System.exit(1);

    // Experiment IL fast read
    long fast_il = algo.fast_il(N_EXPERIMENTS);
    System.out.println((float)fast_il);

    // Experiment complete IL read
    long complete_il = algo.complete_il(N_EXPERIMENTS);
    System.out.println((float)complete_il);

    // Experiment P-SPACE READ
    long p_space = algo.p_space(N_EXPERIMENTS);
    System.out.println((float)p_space);
  }

}
