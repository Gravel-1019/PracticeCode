package com.gravel.shucheng;

import java.util.ArrayList;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        ArrayList list = new ArrayList();
        while (true){
            System.out.println("1.展示书籍");
            System.out.println("2.上新书籍");
            System.out.println("3.下架书籍");
            System.out.println("4.退出应用");
            Scanner sc = new Scanner(System.in);
            System.out.print("请输入序号:");
            int choice = sc.nextInt();
            if (choice == 1) {
                System.out.println("[gravel书城] >>>>>1.展示书籍");

                if (list.size() == 0){
                    System.out.println("暂时没有书籍！");
                    continue;
                }
                for (int i = 0; i < list.size();i++){
                    Book b = (Book) (list.get(i));
                    System.out.println(b.getbNo() + "-----" + b.getbName() + "-----" + b.getbAuthor());
                }
            }
            if (choice == 2) {
                System.out.println("[gravel书城] >>>>>2.上新书籍");
                System.out.print("请输入书籍编号:");
                int bNo = sc.nextInt();
                System.out.print("请输入书籍名字:");
                String bName = sc.next();
                System.out.print("请输入书籍作者:");
                String bAuthor = sc.next();
                Book b = new Book();
                b.setbNo(bNo);
                b.setbName(bName);
                b.setbAuthor(bAuthor);

                list.add(b);
            }
            if (choice == 3) {
                System.out.println("[gravel书城] >>>>>3.下架书籍");
                System.out.print("输入编号:");
                int delNo = sc.nextInt();
                for (int i = 0; i < list.size();i++){
                    Book b = (Book) (list.get(i));
                    if (b.getbNo() == delNo){
                        list.remove(b);
                        System.out.println("书籍下架成功！");
                        break;
                    }
                }
            }
            if (choice == 4) {
                System.out.println("[gravel书城] >>>>>4.退出应用");
                break;
            }
        }

    }
}
