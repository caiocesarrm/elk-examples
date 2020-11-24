using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace elk_netcore.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger)
        {
            _logger = logger;
        }

        [HttpGet("GetPadrao")]
        public IEnumerable<WeatherForecast> GetPadrao()
        {
            var rng = new Random();

            _logger.LogDebug("Este é um log de DEBUG");
            _logger.LogInformation("Este é um log de INFO");
            _logger.LogWarning("Este é um log de WARNING");
            _logger.LogError("Este é um log de ERROR");
            _logger.LogCritical("Este é um log de CRITICAL");
            
            return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-20, 55),
                Summary = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }


        [HttpGet]
        public ActionResult Get()
        {
           
            _logger.LogDebug("Este é um log de DEBUG");
            _logger.LogInformation("Este é um log de INFO");
            _logger.LogWarning("Este é um log de WARNING");
            _logger.LogError("Este é um log de ERROR");
            _logger.LogCritical("Este é um log de CRITICAL");

            return Ok(new { Sucess = true });
        }


    }
}
