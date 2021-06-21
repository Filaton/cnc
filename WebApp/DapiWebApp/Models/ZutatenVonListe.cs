using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DapiWebApp.Models
{
    public class ZutatenVonListe
    {
        public int CocktailID { get; set; }
        public int ZutatID { get; set; } 
        public int Menge { get; set; }
    }
}
