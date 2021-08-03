using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DapiWebApp.Models
{
    public class Zutaten
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Flasche { get; set; }

        public string Image { get; set; }
    }
}
