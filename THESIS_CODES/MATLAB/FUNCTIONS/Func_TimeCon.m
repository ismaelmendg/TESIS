
function DataOut = Func_TimeCon(seconds, NPoint, Nsample)

    T = (seconds/Nsample)/NPoint;
    DataOut = (0:T:seconds)';
    
end