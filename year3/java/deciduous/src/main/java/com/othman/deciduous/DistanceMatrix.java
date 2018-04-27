package com.othman.deciduous;


import com.google.gson.GsonBuilder;
import com.google.maps.DistanceMatrixApi;
import com.google.maps.DistanceMatrixApiRequest;
import com.google.maps.GeoApiContext;
import com.google.maps.model.LatLng;

// TODO: Possibly include POST instead of GET?
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;


@Path("/distances")
@Produces(MediaType.APPLICATION_JSON)
public class DistanceMatrix {

    //TODO: Omit URL and OUTPUT_TYPE strings
    public static final String URL = "https://maps.googleapis.com/maps/api/geocode";
    public static final String OUTPUT_TYPE = "json";
    private static final String API_KEY = "AIzaSyDs9vEjMdRpvj3wAlBrk1TjTHQtSbTNwAE";

    @GET
    public String getDistances(@QueryParam("origins") String origins,
                               @QueryParam("destinations") String destinations)
    {
        GeoApiContext context = new GeoApiContext().setApiKey(API_KEY);

        LatLng origin1 = new LatLng(55.930385, -3.118425);
        String origin2 = "Greenwich, England";
        String destinationA = "Stockholm, Sweden";
        LatLng destinationB = new LatLng(50.087692, 14.421150);


        DistanceMatrixApiRequest matrix = DistanceMatrixApi.getDistanceMatrix(context,
                new String[]{"Sydney Town Hall"},
                new String[]{"Parramatta Station"});

        System.out.println(matrix);
        return matrix.toString();
    }
}
