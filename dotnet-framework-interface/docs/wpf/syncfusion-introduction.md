<h1 class="heading"><span class="name">Syncfusion Libraries</span></h1>

Under a licensing agreement with Syncfusion, Dyalog includes the Syncfusion library of WPF controls. These may be used by Dyalog APL users to develop applications, and may be distributed with Dyalog APL run-time applications.

The Syncfusion libraries comprise a set of .NET assemblies which are supplied in the *Syncfusion/4.6* sub-directory of the main Dyalog APL installation directory (for example: *c:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\Syncfusion\4.6*.

## Requirements

To use the Syncfusion libraries you must be using Microsoft .NET Version 4.5.

In addition, to use the controls contained in these assemblies it is necessary to perform one or both of the following steps.

## Using XAML

If using XAML, the XAML must include the appropriate `xmlns` statements that specify where the Syncfusion controls are to be found. For example:
```xml
xmlns:syncfusion="clr-namespace:Syncfusion.Windows.Gauge;
                  assembly=Syncfusion.Gauge.WPF"
```

The above statement defines the prefix `syncfusion` to mean the specified Syncfusion namespace and assembly that contains the various Gauge controls. When the prefix `syncfusion` is subsequently used in front of a control in the XAML, the system knows where to find it. For example:
```apl
<syncfusion:CircularGauge Name="fahrenheit" Margin="10">
```

## ⎕USING

In common with all .NET types, when a Syncfusion control is loaded using XAML or using `⎕NEW` it is essential that the current value of `⎕USING` identifies the .NET namespace and assembly in which the control will be found. For example:
```apl

       ⎕USING,←⊂'Syncfusion.Windows.Gauge,Syncfusion/4.6/Syncfusion.Gauge.WPF.dll'
```

This statement tells APL to search the .NET namespace named *Syncfusion.Windows.Gauge*, which is located in the assembly file whose path (relative to the Dyalog installation directory) is  `Syncfusion/4.6/Syncfusion.Gauge.WPF.dll`.
