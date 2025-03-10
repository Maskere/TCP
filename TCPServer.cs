using System.Net.Sockets;

namespace TCP{
    public class TCPServer{
        public static void HandleClient(TcpClient socket, int port){
            bool isRunning = true;

            using(socket){
                NetworkStream ns = socket.GetStream();

                StreamReader reader = new(ns);
                StreamWriter writer = new(ns);
                writer.AutoFlush = true;

                while(isRunning){
                    string? request = reader.ReadLine();

                    if(request != null){
                        request.Trim();

                        if(request == "Random" ||
                                request == "Add" ||
                                request == "Subtract"){
                            HandleIncomingMessage(writer,reader,request);
                        }
                        else{
                            writer.Write($"Server response: {request}");
                        }
                    }
                    else{
                        writer.Write("Bad request");
                    }
                }
            }
        }

        static void HandleIncomingMessage(StreamWriter writer, StreamReader reader, string? request){
            Random random = new();
            if(request != null){
                writer.Write("Input numbers");

                string? numbers = reader.ReadLine();

                if(numbers != null){
                    string[] splitNumbers = numbers.Split(" ");

                    if(int.TryParse(splitNumbers?[0], out int firstResult)){
                        if(int.TryParse(splitNumbers?[1].Trim(), out int secondResult)){
                            if(request == "Random"){
                                if(firstResult > secondResult){
                                    writer.Write("First number:{0} numbers must be greater than second number:{1}",firstResult,secondResult);
                                }
                                else{
                                    int randomResult = random.Next(firstResult, secondResult + 1);
                                    writer.Write($"Random result: {randomResult}");
                                }
                            }
                            else if(request == "Add"){
                                int addResult = firstResult + secondResult;
                                writer.Write($"Add result: {addResult}");
                            }
                            else if(request == "Subtract"){
                                int subtractResult = firstResult - secondResult;
                                writer.Write($"Subtract result: {subtractResult}");
                            }
                        }
                        else{
                            writer.Write("Second input: '{0}' must be a number",splitNumbers?[1]);
                        }
                    }
                    else{
                        writer.Write("First input: '{0}' must be a number",splitNumbers?[0]);
                    }
                }
            }
        }
    }
}
