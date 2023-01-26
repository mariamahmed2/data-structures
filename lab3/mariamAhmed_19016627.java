import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.awt.*;
import java.util.Scanner;


interface IPlayersFinder {

    java.awt.Point[] findPlayers(String[] photo, int team, int threshold);
}



public class playersFinder implements IPlayersFinder {

    public static void main(String[] args){
        // get the photo dimentions
        Scanner input = new Scanner(System.in);
        String dim = input.nextLine();

        // handel the comma-space separated input using regix
        String[] dimentions = dim.split(",");
        // det the num of rows
        int lines = Integer.parseInt(dimentions[0]);

        // get the photo parameters
        String[] boardPhoto = new String[lines];
        for (int i = 0; i < lines; i++) {
            boardPhoto[i] = input.nextLine();
        }

        // input the team number and the min area
        int team = Integer.parseInt(input.nextLine());
        int minArea = Integer.parseInt(input.nextLine());

        IPlayersFinder finder = new playersFinder();
        Point[] finalPoints = finder.findPlayers(boardPhoto, team, minArea);

        printPoints(finalPoints);

    }

    // print the final points as required in a list of tuples
    private static void printPoints(Point[] finalPoints) {
        StringBuilder ListOfPoints = new StringBuilder("[");
        for (int i = 0; i < finalPoints.length; i++) {
            // tuples creation (x, y) format
            if (i < finalPoints.length - 1)
                ListOfPoints.append("(").append(finalPoints[i].x).append(", ").append(finalPoints[i].y).append("), ");
            else
                ListOfPoints.append("(").append(finalPoints[i].x).append(", ").append(finalPoints[i].y).append(")");
        }
        ListOfPoints.append("]");
        System.out.println(ListOfPoints);
    }
    
    // variables for the bounded box limits
    private  int upperI;
    private int UpperJ;
    private int LowerI;
    private int LowerJ;
    private int minArea;
    @Override
    public java.awt.Point[] findPlayers(String[] photo,int team,int AreaThreshold){
        // define the limits of the bounded box
        int xBound = colsNum(photo);
        int yBound = rowsNum(photo);
        // handel the input constrains: "Dimensions of the photo will be between 1 and 50 elements. Minimum area for an element will be between 1 and 10000 inclusive"

        if (AreaThreshold<1||AreaThreshold>1000|| yBound >50|| xBound >50){
            return null;
        }
        else {
            int minArea = 100000;
            Point[] players = new Point[minArea];
            boolean[][] visited;
            visited = changeToSparse(photo, team, xBound, yBound);
            int playersNum = 0;
            // find the total boxes among the photo
            for (int i = 0; i < xBound; i++) {
                for (int j = 0; j < yBound; j++) {
                    UpperJ = j;
                    upperI = i;
                    LowerJ = j;
                    LowerI = i;
                    this.minArea = 0;
                    findTotalBox(visited, xBound, yBound, i, j);
                    if (this.minArea >= AreaThreshold) {
                        players[playersNum] = new Point();
                        players[playersNum].setLocation((upperI + LowerI + 1), (UpperJ + LowerJ + 1));
                        playersNum++;
                    }
                }
            }


            Point[] NoPhotoPlayers = new Point[playersNum];

            // function to sort the players' points
            playersPointsSort(players, playersNum);
            // handel the no player condition
            if (playersNum == 0)
                return null;
            for (int i = 0; i < playersNum; i++) {
                NoPhotoPlayers[i] = new Point();
                NoPhotoPlayers[i].setLocation(players[i]);
            }
            return NoPhotoPlayers;
        }
    }
    //calculte number of rows
    public int rowsNum (String[] result){
        int NumRows = 0;
        for(int i = 0; i< result.length; i++){
            NumRows++;
        }
        return NumRows;
    }

    //calculate number of colums
    public int colsNum (String[] result){
        String NumCols = result[0];
        return NumCols.length();
    }


    // define the sparse array
    boolean[][] changeToSparse(String[] photo, int teamId, int UpperX, int UpperY) {

        boolean[][] BoundedArr = new boolean[UpperX][UpperY];
        for(int i=0; i< UpperX; i++) {
            for(int j=0; j< UpperY; j++) {

                BoundedArr[i][j]= (Character.getNumericValue(photo[j].charAt(i))) == teamId;
            }
        }
        return BoundedArr;
    }

    // function to sort the players' points
    void playersPointsSort(Point[] teamPlayers, int PointsPlayers) {
        Point addArr = new Point();
        for(int rows = 0; rows < PointsPlayers; rows++) {
            for(int cols = 0; cols < PointsPlayers - rows -1; cols++) {
                if(teamPlayers[cols].getX()> teamPlayers[cols +1].getX()||((teamPlayers[cols].getX()== teamPlayers[cols +1].getX())&& teamPlayers[cols].getY()> teamPlayers[cols +1].getY())) {
                    addArr.setLocation(teamPlayers[cols +1]);
                    teamPlayers[cols +1].setLocation(teamPlayers[cols]);
                    teamPlayers[cols].setLocation(addArr);
                }
            }
        }
    }

    // get the box that lower than the threshold of area out
    //return the elements of indexs
    void findTotalBox(boolean[][] ArrSparse, int UpperX, int UpperY, int row, int col){
        if(ArrSparse[row][col]) {
            ArrSparse[row][col]=false;
            if(row > upperI)
                upperI = row;
            else if(col > UpperJ)
                UpperJ = col;
            else if(col < LowerJ)
                LowerJ = col;
            else if(row < LowerI)
                LowerI = row;
            minArea +=4;
            if(row +1< UpperX)
                findTotalBox(ArrSparse, UpperX, UpperY, row +1, col);
            if(row -1>-1)
                findTotalBox(ArrSparse, UpperX, UpperY, row -1, col);
            if(col +1< UpperY)
                findTotalBox(ArrSparse, UpperX, UpperY, row, col +1);
            if((col -1)>-1)
                findTotalBox(ArrSparse, UpperX, UpperY, row, col -1);
        }
    }

   
}





