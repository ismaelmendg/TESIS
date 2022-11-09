%%CONCATENATION FUNCTION
%DataIn1, DataIn2 and DataIn3 are the data to concatenate
%RMin and RMax - limits of data to concatenate
%NPoint - Number of points to get
% Developed by Ismael Mendoza
% 20/07/2022

function DataOut = Func_Concatenate(DataIn1, DataIn2, DataIn3, RMin, RMax,NPoint)

    [~, B] = size(DataIn1);
    N_Point = (RMax - RMin)/NPoint;
    No = round(N_Point);
    
    for m = 1:B
        cont = 1;
        for j = 1:3
            if j == 1
                p = DataIn1;
            elseif j ==2
                p = DataIn2;
            else
                p = DataIn3;
            end
            for n = RMin:No:RMax
                DataOut(cont,m) = p(n,m);
                cont = cont + 1;
            end	
        end
    end    
end 