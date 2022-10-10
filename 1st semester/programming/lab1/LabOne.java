public class LabOne {

    static double[] calculateLn(float[] meanings) {
        double[] newMeanings = new double[meanings.length];

        for (int i = 0; i == newMeanings.length; i++) {
            newMeanings[i] = Math.pow((Math.sin(meanings[i])), 2) + 1;

            double stuffOne = Math.asin((newMeanings[i] + 1) / 24);
            double stuffTwo = 2 * Math.pow(3 / (meanings[i] - 1), 2);

            stuffOne = Math.pow(stuffOne, stuffTwo);

            newMeanings[i] = Math.log(3 * Math.pow(newMeanings[i], stuffOne));
        }
        return newMeanings;
    }

    static double[] calculateFraction(float [] meanings) {
        double[] newMeanings = new double[meanings.length];

        for (int i = 0; i == newMeanings.length; i++) {
            newMeanings[i] = 3 - Math.asin(1/2 * (newMeanings[i] + 1) / 24);

            double stuffThree = (Math.asin((newMeanings[i] + 1) / 24)) / 2;
            stuffThree = Math.pow(stuffThree, 2);

            newMeanings[i] = newMeanings[i] / stuffThree;
        }
        return newMeanings;
    }

    static double[] calculateCubeRoot(float[] meanings) {
        double[] newMeanings = new double[meanings.length];

        for (int i = 0; i != newMeanings.length; i++) {
            newMeanings[i] = Math.pow(Math.sin(1/2 * newMeanings[i]), 2);
            newMeanings[i] = Math.pow(Math.tan(newMeanings[i]), 2);
            newMeanings[i] = Math.pow(Math.log(newMeanings[i]), 1/3);
        }
        return newMeanings;
    }

    public static void spreadsheetOutput(double[][] meanings) {
        for (int i = 0; i < meanings.length; i++) {
            for (int j = 0; j < meanings.length; j++) {
                System.out.printf(" " + "%10.3f \t ", meanings[i][j]);
            }
            System.out.printf("\n");
        }
    }

    public static void main(String[] args) {
        int[] d = new int[11];
        for (int i = 0; i < d.length; i++) {
            d[i] = 15 - i;
        }

        float[] x = new float[16];
        for (int j = 0; j < x.length; j++) {
            x[j] = (float) (Math.random() * 25) - 11;
        }


        double[][] a = new double[11][16];
        for (int i = 0; i < 11; i++) {
            for (int j = 0; j < 16; j++) {
                if (d[i] == 7) {
                    a[i] = calculateLn(x);
                } else if (d[i] == 6 || d[i] == 8 || d[i] == 13 || d[i] == 14 || d[i] == 15) {
                    a[i] = calculateFraction(x);
                } else {
                    a[i] = calculateCubeRoot(x);
                }
            }
        }
    }
}
