using System;

public class SlotMachine
{
    public static void Main(string[] args)
    {
        Random random = new Random();
        string[] slots = { "Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar" };
        string[] result = new string[3];

        for (int i = 0; i < 3; i++)
        {
            int index = random.Next(slots.Length);
            result[i] = slots[index];
        }

        Console.WriteLine("Welcome to Christopher Buss Casino!");
        Console.WriteLine("Spinning the slots...");
        Console.WriteLine($"{result[0]} | {result[1]} | {result[2]}");

        if (result[0] == result[1] && result[1] == result[2])
        {
            Console.WriteLine("Congratulations! You hit the jackpot!");
        }
        else
        {
            Console.WriteLine("Better luck next time!");
        }
    }
}