%%FUNCTION TO COLLECT DATA FROM THE TRIGGER
%Main - Original main array
%column - Column number containing the trigger data
%Trigger_value - Trigger value to search for data collection
%DataIn - Matrix from which the data will be collected
%RMin and RMax - Data collection limits
%RPMin and RPMax - Data collection limits to adjust
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Gather(Main, column, Trigger_value, DataIn, RMin, RMax, RPMin, RPMax)

    Data = [];
    Temp = find(Main(:,column) == Trigger_value);
    for n = 1:length(Temp)
        Data(:,n) = [DataIn(Temp(n,1)+RMin:Temp(n,1)+RMax)];
    end

    DataOut = Data;
    
end

