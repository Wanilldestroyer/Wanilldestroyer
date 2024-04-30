using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Введите массив из нулей и единиц (без пробелов):");
        string binaryInput = Console.ReadLine();

        try
        {
            int decimalNumber = Convert.ToInt32(binaryInput, 2);

            if (decimalNumber >= 0 && decimalNumber <= 100)
                Console.WriteLine("Число в диапазоне от 0 до 100." + decimalNumber);
            else
                Console.WriteLine("Число вне диапазона от 0 до 100." + decimalNumber);

            Console.Write($"{Environment.NewLine}Press any key to exit...");
            Console.ReadKey(true);
        }
        catch (FormatException)
        {
            Console.WriteLine("Неправильный ввод. Введите только нули и единицы без пробелов.");
        }
    }
}