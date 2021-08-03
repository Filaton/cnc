using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DapiWebApp.Services
{
    public class AppState
    {
        public int[] AusgewaehlteSchnaepse = new int[16];
        public int[,] MappedSorten = new int[16, 2];
    }
}
